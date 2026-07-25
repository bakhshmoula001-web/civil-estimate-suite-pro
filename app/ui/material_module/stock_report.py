
from openpyxl import Workbook

class StockReport:
    def export_excel(self, rows, filename):
        wb=Workbook()
        ws=wb.active
        ws.append(["Date","Reference","Receipt","Issue","Balance"])
        for r in rows:
            ws.append([r["date"],r["reference"],r["receipt"],r["issue"],r["balance"]])
        wb.save(filename)
        return filename
