class VendorService:
    def __init__(self, db):
        self.db=db

    def get_all(self):
        return self.db.fetch_all("SELECT * FROM vendors ORDER BY name")

    def add(self,data):
        self.db.execute(
            "INSERT INTO vendors(name,contact,phone,address) VALUES(?,?,?,?)",
            (data["name"],data["contact"],data["phone"],data["address"])
        )

    def update(self,vendor_id,data):
        self.db.execute(
            "UPDATE vendors SET name=?,contact=?,phone=?,address=? WHERE id=?",
            (data["name"],data["contact"],data["phone"],data["address"],vendor_id)
        )

    def delete(self,vendor_id):
        self.db.execute("DELETE FROM vendors WHERE id=?", (vendor_id,))
