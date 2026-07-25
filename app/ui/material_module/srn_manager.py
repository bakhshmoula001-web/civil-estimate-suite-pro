from datetime import date

class SRNManager:
    def create(self, department, items):
        return {
            "srn_no": f"SRN-{date.today():%Y%m%d}",
            "department": department,
            "date": str(date.today()),
            "items": items
        }
