from app.database.connection import get_connection
from app.database.connection import DatabaseConnection

class ProjectService:

    def __init__(self):
        self.conn = DatabaseConnection().connect()

    def count_projects(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM projects")
        return cursor.fetchone()[0] or 0

    def total_project_cost(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT COALESCE(SUM(total_cost),0) FROM projects")
        return cursor.fetchone()[0]

    def get_recent_projects(self, limit=10):
        cursor = self.conn.cursor()

        cursor.execute("""
            SELECT project_code,
                   project_name,
                   status
            FROM projects
            ORDER BY id DESC
            LIMIT ?
        """, (limit,))

        return cursor.fetchall()