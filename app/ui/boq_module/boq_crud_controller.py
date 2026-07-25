class BOQCRUDController:
    def __init__(self, form, table, service):
        self.form=form
        self.table=table
        self.service=service
        self.current_id=None

    def refresh(self):
        self.table.load(self.service.get_all_items())

    def add(self):
        data=self.form.get_data()
        self.service.add_item(data)
        self.form.clear()
        self.refresh()

    def edit(self, item_id):
        row=self.service.get_item(item_id)
        if row:
            self.current_id=item_id
            self.form.set_data(row)

    def update(self):
        if self.current_id is None:
            return
        self.service.update_item(self.current_id, self.form.get_data())
        self.current_id=None
        self.form.clear()
        self.refresh()

    def delete(self, item_id):
        self.service.delete_item(item_id)
        self.refresh()
