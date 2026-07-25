from boq_excel_export import BOQExcelExporter
from boq_pdf_export import BOQPDFExporter

class BOQReportManager:
    def __init__(self):
        self.excel=BOQExcelExporter()
        self.pdf=BOQPDFExporter()

    def export_excel(self, items, filename):
        return self.excel.export(items, filename)

    def export_pdf(self, items, filename):
        return self.pdf.export(items, filename)

    def summary(self, items):
        total=sum(float(i.get("amount",0)) for i in items)
        return {
            "items": len(items),
            "grand_total": round(total,2)
        }
