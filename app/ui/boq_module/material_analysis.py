class MaterialAnalysis:
    def summarize(self, items):
        totals={}
        for item in items:
            mats=item.get("materials",{})
            for name,qty in mats.items():
                totals[name]=totals.get(name,0)+float(qty)
        return totals
