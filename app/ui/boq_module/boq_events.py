class BOQEvents:
    def __init__(self, controller):
        self.controller=controller

    def save(self):
        if self.controller.current_id is None:
            self.controller.add()
        else:
            self.controller.update()

    def refresh(self):
        self.controller.refresh()

    def delete_selected(self):
        row=self.controller.table.selected()
        if row:
            self.controller.delete(int(row[0]))
