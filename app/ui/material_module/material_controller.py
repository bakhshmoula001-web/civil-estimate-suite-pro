class MaterialController:
    def __init__(self,form,table,service):
        self.form=form
        self.table=table
        self.service=service
        self.current_id=None

    def refresh(self):
        self.table.load(self.service.get_all())

    def save(self):
        data=self.form.get_data()
        if self.current_id is None:
            self.service.add(data)
        else:
            self.service.update(self.current_id,data)
            self.current_id=None
        self.form.clear()
        self.refresh()

    def edit_selected(self):
        row=self.table.selected()
        if not row:
            return
        self.current_id=row[0]
        self.form.set_data({
            "code":row[1],
            "name":row[2],
            "unit":row[3],
            "rate":row[4]
        })

    def delete_selected(self):
        row=self.table.selected()
        if row:
            self.service.delete(row[0])
            self.refresh()
