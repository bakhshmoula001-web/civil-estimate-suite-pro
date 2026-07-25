from openpyxl import Workbook

class VoucherExporter:
    def export_excel(self, voucher, filename):
        wb=Workbook()
        ws=wb.active
        ws.append(["Field","Value"])
        for k,v in voucher.items():
            if k!="items":
                ws.append([k,str(v)])
        ws.append([])
        ws.append(["Item","Quantity"])
        for item in voucher.get("items",[]):
            ws.append([item.get("name",""), item.get("qty","")])
        wb.save(filename)
        return filename
