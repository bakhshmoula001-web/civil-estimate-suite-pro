class BOQSummary:
    def generate(self, items):
        total_qty=sum(float(i.get("quantity",0)) for i in items)
        total_amount=sum(float(i.get("amount",0)) for i in items)
        return {
            "items": len(items),
            "quantity": round(total_qty,2),
            "amount": round(total_amount,2)
        }
