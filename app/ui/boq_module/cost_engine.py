class CostEngine:
    @staticmethod
    def amount(quantity, rate):
        return round(float(quantity) * float(rate), 2)

    @staticmethod
    def grand_total(items):
        return round(sum(float(i.get("amount", 0)) for i in items), 2)

    @staticmethod
    def cost_breakdown(items):
        material = sum(float(i.get("material_cost", 0)) for i in items)
        labour = sum(float(i.get("labour_cost", 0)) for i in items)
        equipment = sum(float(i.get("equipment_cost", 0)) for i in items)
        return {
            "material": round(material,2),
            "labour": round(labour,2),
            "equipment": round(equipment,2),
            "total": round(material+labour+equipment,2)
        }
