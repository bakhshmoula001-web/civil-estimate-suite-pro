from material_excel_report import MaterialExcelReport
from material_pdf_report import MaterialPDFReport
from material_dashboard_sync import MaterialDashboardSync

class MaterialModule:
    def __init__(self, service):
        self.service = service
        self.excel = MaterialExcelReport()
        self.pdf = MaterialPDFReport()
        self.dashboard = MaterialDashboardSync()

    def export_excel(self, filename):
        return self.excel.export(self.service.get_all(), filename)

    def export_pdf(self, filename):
        return self.pdf.export(self.service.get_all(), filename)

    def dashboard_summary(self):
        return self.dashboard.build_summary(self.service.get_all())
