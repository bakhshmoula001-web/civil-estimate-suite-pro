class MaterialConsumption:
    def summarize(self,boq_items):
        totals={}
        for item in boq_items:
            for mat,qty in item.get("materials",{}).items():
                totals[mat]=totals.get(mat,0)+float(qty)
        return totals
