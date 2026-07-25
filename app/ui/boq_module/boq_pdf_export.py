from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

class BOQPDFExporter:
    def export(self, items, filename):
        data=[["Code","Description","Unit","Qty","Rate","Amount"]]
        total=0
        for i in items:
            amt=float(i.get("amount",0))
            total+=amt
            data.append([
                i.get("item_code",""),
                i.get("description",""),
                i.get("unit",""),
                i.get("quantity",""),
                i.get("rate",""),
                amt
            ])
        data.append(["","","","","Grand Total",total])

        table=Table(data)
        table.setStyle(TableStyle([
            ("GRID",(0,0),(-1,-1),0.5,colors.black),
            ("BACKGROUND",(0,0),(-1,0),colors.lightgrey),
            ("BACKGROUND",(0,-1),(-1,-1),colors.beige),
        ]))
        doc=SimpleDocTemplate(filename)
        doc.build([table])
        return filename
