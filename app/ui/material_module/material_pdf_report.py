from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

class MaterialPDFReport:
    def export(self, materials, filename):
        data=[["Code","Material","Unit","Rate","Stock"]]
        for m in materials:
            data.append([
                m.get("code",""),
                m.get("name",""),
                m.get("unit",""),
                m.get("rate",0),
                m.get("stock",0)
            ])

        table=Table(data)
        table.setStyle(TableStyle([
            ("GRID",(0,0),(-1,-1),0.5,colors.black),
            ("BACKGROUND",(0,0),(-1,0),colors.lightgrey)
        ]))

        doc=SimpleDocTemplate(filename)
        doc.build([table])
        return filename
