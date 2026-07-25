class MaterialService:
    def __init__(self,database):
        self.db=database
    def get_all(self):
        return self.db.fetch_all("SELECT * FROM materials ORDER BY name")
    def add(self,data):
        self.db.execute(
            "INSERT INTO materials(code,name,unit,rate) VALUES(?,?,?,?)",
            (data["code"],data["name"],data["unit"],data["rate"])
        )
    def update(self,mid,data):
        self.db.execute(
            "UPDATE materials SET code=?,name=?,unit=?,rate=? WHERE id=?",
            (data["code"],data["name"],data["unit"],data["rate"],mid)
        )
    def delete(self,mid):
        self.db.execute("DELETE FROM materials WHERE id=?",(mid,))
