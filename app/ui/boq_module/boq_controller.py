class BOQController:
    def __init__(self,service,form,table):
        self.service=service; self.form=form; self.table=table
    def refresh(self):
        self.table.load(self.service.get_all_items())
