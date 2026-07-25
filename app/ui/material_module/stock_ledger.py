
from datetime import datetime

class StockLedger:
    def __init__(self):
        self.transactions=[]

    def add_transaction(self, material, trans_type, qty, reference="", warehouse="Main"):
        self.transactions.append({
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "material": material,
            "type": trans_type,
            "qty": float(qty),
            "reference": reference,
            "warehouse": warehouse
        })

    def balance(self, material):
        bal=0
        for t in self.transactions:
            if t["material"]==material:
                bal += t["qty"] if t["type"]=="RECEIPT" else -t["qty"]
        return bal
