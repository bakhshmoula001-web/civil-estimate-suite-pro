from openpyxl import Workbook
from openpyxl.styles import Font

class MaterialExcelReport:
    def export(self, materials, filename):
        wb = Workbook()
        ws = wb.active
        ws.title = "Material Report"

        headers = ["Code","Material","Unit","Rate","Stock"]
        for c,h in enumerate(headers,1):
            cell = ws.cell(row=1,column=c,value=h)
            cell.font = Font(bold=True)

        for m in materials:
            ws.append([
                m.get("code",""),
                m.get("name",""),
                m.get("unit",""),
                m.get("rate",0),
                m.get("stock",0)
            ])

        wb.save(filename)
        return filename
