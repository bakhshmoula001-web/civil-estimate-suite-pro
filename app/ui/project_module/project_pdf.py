from reportlab.platypus import SimpleDocTemplate, Table
from reportlab.lib import colors

class ProjectPDFExporter:
    def export(self, projects, filename):
        data=[["ID","Code","Project","Client","Location","Status"]]
        for p in projects:
            data.append([
                getattr(p,"id",""),
                getattr(p,"project_code",""),
                getattr(p,"project_name",""),
                getattr(p,"client_name",""),
                getattr(p,"location",""),
                getattr(p,"status","")
            ])
        table=Table(data)
        table.setStyle([
            ("GRID",(0,0),(-1,-1),0.5,colors.black),
            ("BACKGROUND",(0,0),(-1,0),colors.lightgrey),
        ])
        doc=SimpleDocTemplate(filename)
        doc.build([table])
        return filename
