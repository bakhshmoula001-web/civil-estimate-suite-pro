from openpyxl import Workbook
from openpyxl.styles import Font

class ProjectExcelExporter:
    HEADERS=[
        "ID","Code","Project","Client",
        "Location","Status","Start Date","End Date"
    ]

    def export(self, projects, filename):
        wb=Workbook()
        ws=wb.active
        ws.title="Projects"

        for c,h in enumerate(self.HEADERS,1):
            cell=ws.cell(row=1,column=c,value=h)
            cell.font=Font(bold=True)

        for r,p in enumerate(projects,2):
            ws.append([
                getattr(p,"id",""),
                getattr(p,"project_code",""),
                getattr(p,"project_name",""),
                getattr(p,"client_name",""),
                getattr(p,"location",""),
                getattr(p,"status",""),
                getattr(p,"start_date",""),
                getattr(p,"end_date","")
            ])
        wb.save(filename)
        return filename
