
from app.models.project import Project

class ProjectCRUDController:
    def __init__(self, form, table, service):
        self.form=form
        self.table=table
        self.service=service
        self.current_id=None

    def load(self):
        self.table.load(self.service.get_all_projects())

    def add(self):
        data=self.form.validate()
        self.service.add_project(Project(**data))
        self.form.clear()
        self.load()

    def edit(self, project_id:int):
        p=self.service.get_project(project_id)
        if not p:
            return
        self.current_id=project_id
        values=p.__dict__.copy()
        remarks=values.pop("remarks","")
        for k,w in self.form.inputs.items():
            w.delete(0,"end")
            w.insert(0, values.get(k,""))
        self.form.remarks.delete("1.0","end")
        self.form.remarks.insert("1.0",remarks)

    def update(self):
        if self.current_id is None:
            return
        data=self.form.validate()
        self.service.update_project(self.current_id, Project(**data))
        self.current_id=None
        self.form.clear()
        self.load()

    def delete(self, project_id:int):
        self.service.delete_project(project_id)
        self.load()
