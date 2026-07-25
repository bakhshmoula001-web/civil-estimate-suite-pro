from project_excel import ProjectExcelExporter
from project_pdf import ProjectPDFExporter
from project_print import ProjectPrintManager

class ProjectModuleIntegration:
    def __init__(self):
        self.excel=ProjectExcelExporter()
        self.pdf=ProjectPDFExporter()
        self.printer=ProjectPrintManager()

    def export_excel(self, projects, filename):
        return self.excel.export(projects, filename)

    def export_pdf(self, projects, filename):
        return self.pdf.export(projects, filename)

    def print_preview(self, projects):
        return self.printer.preview(projects)
