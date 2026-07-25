class MaterialDashboardSync:
    def build_summary(self, materials):
        total_items = len(materials)
        total_stock = sum(float(m.get("stock",0)) for m in materials)
        total_value = sum(
            float(m.get("stock",0))*float(m.get("rate",0))
            for m in materials
        )

        return {
            "total_materials": total_items,
            "total_stock": round(total_stock,2),
            "inventory_value": round(total_value,2)
        }
