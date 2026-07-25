from datetime import date

class GRNManager:
    def create(self, vendor, items, reference):
        return {
            "grn_no": f"GRN-{date.today():%Y%m%d}",
            "vendor": vendor,
            "reference": reference,
            "date": str(date.today()),
            "items": items
        }
