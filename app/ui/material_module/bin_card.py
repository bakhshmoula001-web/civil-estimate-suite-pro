
class BinCard:
    def generate(self, ledger, material):
        rows=[]
        bal=0
        for t in ledger.transactions:
            if t["material"]!=material:
                continue
            bal += t["qty"] if t["type"]=="RECEIPT" else -t["qty"]
            rows.append({
                "date":t["date"],
                "reference":t["reference"],
                "receipt":t["qty"] if t["type"]=="RECEIPT" else 0,
                "issue":t["qty"] if t["type"]=="ISSUE" else 0,
                "balance":bal
            })
        return rows
