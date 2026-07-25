class ProjectController:
    def __init__(self, service, table):
        self.service=service
        self.table=table

    def refresh(self):
        self.table.load(self.service.get_all_projects())

    def search(self,text):
        rows=self.service.get_all_projects()
        text=text.lower().strip()
        if not text:
            self.table.load(rows)
            return
        result=[
            p for p in rows
            if text in p.project_name.lower()
            or text in p.project_code.lower()
            or text in p.client_name.lower()
        ]
        self.table.load(result)
