from app.database.connection import get_connection
from app.database.connection import DatabaseConnection

class MaterialService:

    def __init__(self):
       self.conn = DatabaseConnection().connect()

    def count_materials(self):
        cursor = self.conn.cursor()

        cursor.execute("""
            SELECT COUNT(*)
            FROM materials
        """)

        return cursor.fetchone()[0] or 0

    def total_stock_value(self):
        cursor = self.conn.cursor()

        cursor.execute("""
            SELECT COALESCE(SUM(quantity * rate),0)
            FROM materials
        """)

        return cursor.fetchone()[0]