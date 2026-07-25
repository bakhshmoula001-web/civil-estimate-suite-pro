class BOQService:
    def __init__(self, database):
        self.db = database

    def get_all_items(self):
        return self.db.fetch_all("SELECT * FROM boq_items ORDER BY id")

    def get_item(self, item_id):
        rows=self.db.fetch_all("SELECT * FROM boq_items WHERE id=?", (item_id,))
        return rows[0] if rows else None

    def add_item(self, data):
        sql = '''
        INSERT INTO boq_items
        (project_id,item_code,description,unit,quantity,rate,amount)
        VALUES (?,?,?,?,?,?,?)
        '''
        self.db.execute(sql, (
            data["project_id"], data["item_code"], data["description"],
            data["unit"], data["quantity"], data["rate"], data["amount"]
        ))

    def update_item(self, item_id, data):
        sql = '''
        UPDATE boq_items
        SET item_code=?,description=?,unit=?,quantity=?,rate=?,amount=?
        WHERE id=?
        '''
        self.db.execute(sql, (
            data["item_code"], data["description"], data["unit"],
            data["quantity"], data["rate"], data["amount"], item_id
        ))

    def delete_item(self, item_id):
        self.db.execute("DELETE FROM boq_items WHERE id=?", (item_id,))
