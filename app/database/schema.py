"""
schema.py
Civil Estimate Suite Pro v3.0
Enterprise Database Schema
"""

from __future__ import annotations
import sqlite3
from pathlib import Path


class DatabaseSchema:
    def __init__(self, db_path="data/civil_estimate.db"):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)

    def initialize(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("PRAGMA foreign_keys = ON;")
            self._create_projects(conn)
            self._create_boq(conn)
            self._create_materials(conn)
            self._create_structural(conn)
            self._create_cost(conn)
            self._create_company(conn)
            self._create_settings(conn)
            self._create_indexes(conn)
            conn.commit()

    def _create_projects(self, conn):
        conn.execute("""
        CREATE TABLE IF NOT EXISTS projects(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_code TEXT UNIQUE,
            project_name TEXT NOT NULL,
            client_name TEXT,
            consultant TEXT,
            contractor TEXT,
            location TEXT,
            start_date TEXT,
            end_date TEXT,
            status TEXT DEFAULT 'Planning',
            remarks TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

    def _create_boq(self, conn):
        conn.execute("""
        CREATE TABLE IF NOT EXISTS boq_items(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id INTEGER NOT NULL,
            item_no TEXT,
            description TEXT NOT NULL,
            unit TEXT,
            quantity REAL DEFAULT 0,
            rate REAL DEFAULT 0,
            amount REAL DEFAULT 0,
            remarks TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(project_id) REFERENCES projects(id)
            ON DELETE CASCADE
        )
        """)

    def _create_materials(self, conn):
        conn.execute("""
        CREATE TABLE IF NOT EXISTS materials(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id INTEGER,
            material_name TEXT,
            unit TEXT,
            quantity REAL,
            rate REAL,
            amount REAL,
            FOREIGN KEY(project_id) REFERENCES projects(id)
            ON DELETE CASCADE
        )
        """)

    def _create_structural(self, conn):
        conn.execute("""
        CREATE TABLE IF NOT EXISTS structural_reports(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id INTEGER,
            member_name TEXT,
            specification TEXT,
            quantity REAL,
            remarks TEXT,
            FOREIGN KEY(project_id) REFERENCES projects(id)
            ON DELETE CASCADE
        )
        """)

    def _create_cost(self, conn):
        conn.execute("""
        CREATE TABLE IF NOT EXISTS cost_reports(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id INTEGER,
            category TEXT,
            amount REAL,
            remarks TEXT,
            FOREIGN KEY(project_id) REFERENCES projects(id)
            ON DELETE CASCADE
        )
        """)

    def _create_company(self, conn):
        conn.execute("""
        CREATE TABLE IF NOT EXISTS company(
            id INTEGER PRIMARY KEY CHECK(id=1),
            company_name TEXT,
            address TEXT,
            phone TEXT,
            email TEXT,
            logo TEXT
        )
        """)

    def _create_settings(self, conn):
        conn.execute("""
        CREATE TABLE IF NOT EXISTS settings(
            setting_key TEXT PRIMARY KEY,
            setting_value TEXT
        )
        """)

    def _create_indexes(self, conn):
        conn.execute("CREATE INDEX IF NOT EXISTS idx_project_name ON projects(project_name)")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_boq_project ON boq_items(project_id)")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_material_project ON materials(project_id)")

if __name__ == "__main__":
    DatabaseSchema().initialize()
    print("Database schema initialized successfully.")
