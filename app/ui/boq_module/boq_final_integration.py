from boq_report_manager import BOQReportManager

class BOQModule:
    def __init__(self, service, controller):
        self.service=service
        self.controller=controller
        self.reports=BOQReportManager()

    def refresh(self):
        self.controller.refresh()

    def export_excel(self, filename):
        items=self.service.get_all_items()
        return self.reports.export_excel(items, filename)

    def export_pdf(self, filename):
        items=self.service.get_all_items()
        return self.reports.export_pdf(items, filename)
