"""
connection.py
Civil Estimate Suite Pro v3.0

Central SQLite Connection Manager
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

class DatabaseConnection:
    """
    Central database connection manager.

    All services should obtain database connections
    from this class.
    """

    def __init__(self, db_path: str = "data/civil_estimate.db"):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)

    def connect(self) -> sqlite3.Connection:
        """
        Create and return a configured SQLite connection.
        """
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON;")
        return conn

    def cursor(self):
        """
        Return a cursor object.
        """
        conn = self.connect()
        return conn, conn.cursor()

    def commit(self, conn: sqlite3.Connection):
        """
        Commit current transaction.
        """
        if conn:
            conn.commit()

    def rollback(self, conn: sqlite3.Connection):
        """
        Rollback current transaction.
        """
        if conn:
            conn.rollback()

    def close(self, conn: sqlite3.Connection):
        """
        Safely close connection.
        """
        if conn:
            conn.close()

    def test_connection(self) -> bool:
        """
        Verify that database is reachable.
        """
        conn = None
        try:
            conn = self.connect()
            conn.execute("SELECT 1")
            return True
        except sqlite3.Error:
            return False
        finally:
            if conn:
                conn.close()
def get_connection():
    return DatabaseConnection().connect()


if __name__ == "__main__":
    db = DatabaseConnection()

    if db.test_connection():
        print("✓ Database connection successful.")
    else:
        print("✗ Database connection failed.")
def get_connection():
    """
    Backward compatibility helper.
    """
    return DatabaseConnection().connect()