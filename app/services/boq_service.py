from app.database.connection import get_connection

from app.database.connection import DatabaseConnection
class BOQService:

    def __init__(self):
        self.conn = DatabaseConnection().connect()

    def count_items(self):
        cursor = self.conn.cursor()

        cursor.execute("""
            SELECT COUNT(*)
            FROM boq
        """)

        return cursor.fetchone()[0] or 0

    def total_cost(self):
        cursor = self.conn.cursor()

        cursor.execute("""
            SELECT COALESCE(SUM(amount),0)
            FROM boq
        """)

        return cursor.fetchone()[0]