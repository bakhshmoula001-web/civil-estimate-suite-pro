"""
database.py
Civil Estimate Suite Pro v3.0

Reusable SQLite database manager.
"""

from __future__ import annotations
import sqlite3
from pathlib import Path
from contextlib import contextmanager


class Database:
    """Base database class for all services."""

    def __init__(self, db_path="data/civil_estimate.db"):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)

    @contextmanager
    def connection(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON;")
        try:
            yield conn
            conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()

    def execute(self, query, params=()):
        with self.connection() as conn:
            cur = conn.execute(query, params)
            return cur.lastrowid

    def executemany(self, query, rows):
        with self.connection() as conn:
            conn.executemany(query, rows)

    def fetch_one(self, query, params=()):
        with self.connection() as conn:
            return conn.execute(query, params).fetchone()

    def fetch_all(self, query, params=()):
        with self.connection() as conn:
            return conn.execute(query, params).fetchall()

    def execute_script(self, script: str):
        with self.connection() as conn:
            conn.executescript(script)

    def scalar(self, query, params=(), default=None):
        row = self.fetch_one(query, params)
        if row is None:
            return default
        value = row[0]
        return default if value is None else value

    def exists(self, table, where="1=1", params=()):
        sql = f"SELECT EXISTS(SELECT 1 FROM {table} WHERE {where})"
        return bool(self.scalar(sql, params, False))

    def count(self, table, where=None, params=()):
        sql = f"SELECT COUNT(*) FROM {table}"
        if where:
            sql += f" WHERE {where}"
        return self.scalar(sql, params, 0)

    def delete(self, table, where, params=()):
        sql = f"DELETE FROM {table} WHERE {where}"
        self.execute(sql, params)

    def update(self, table, data: dict, where, where_params=()):
        if not data:
            return
        fields = ", ".join(f"{k}=?" for k in data.keys())
        values = list(data.values()) + list(where_params)
        sql = f"UPDATE {table} SET {fields} WHERE {where}"
        self.execute(sql, values)

    def insert(self, table, data: dict):
        cols = ", ".join(data.keys())
        placeholders = ", ".join(["?"] * len(data))
        sql = f"INSERT INTO {table} ({cols}) VALUES ({placeholders})"
        return self.execute(sql, tuple(data.values()))


if __name__ == "__main__":
    db = Database()
    print("Projects table exists:", db.exists("sqlite_master", "type='table' AND name='projects'"))
