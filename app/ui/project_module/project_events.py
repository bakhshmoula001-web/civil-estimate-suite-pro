
class ProjectEvents:
    def __init__(self, controller):
        self.controller=controller

    def on_new(self):
        self.controller.form.clear()

    def on_save(self):
        if self.controller.current_id is None:
            self.controller.add()
        else:
            self.controller.update()

    def on_delete(self):
        row=self.controller.table.selected()
        if row:
            self.controller.delete(int(row[0]))

    def on_refresh(self):
        self.controller.load()

    def on_double_click(self,row):
        self.controller.edit(int(row[0]))
