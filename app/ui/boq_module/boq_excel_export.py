from openpyxl import Workbook
from openpyxl.styles import Font

class BOQExcelExporter:
    HEADERS=["Code","Description","Unit","Qty","Rate","Amount"]

    def export(self, items, filename):
        wb=Workbook()
        ws=wb.active
        ws.title="BOQ"

        for c,h in enumerate(self.HEADERS,1):
            cell=ws.cell(row=1,column=c,value=h)
            cell.font=Font(bold=True)

        total=0
        for item in items:
            amount=float(item.get("amount",0))
            total+=amount
            ws.append([
                item.get("item_code",""),
                item.get("description",""),
                item.get("unit",""),
                item.get("quantity",""),
                item.get("rate",""),
                amount
            ])

        ws.append([])
        ws.append(["","","","","Grand Total",total])
        wb.save(filename)
        return filename
