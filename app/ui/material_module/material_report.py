from openpyxl import Workbook

class MaterialReport:
    def export_excel(self,summary,filename):
        wb=Workbook()
        ws=wb.active
        ws.append(["Material","Quantity"])
        for k,v in summary.items():
            ws.append([k,v])
        wb.save(filename)
        return filename
