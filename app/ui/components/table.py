import tkinter.ttk as ttk
class DataTable(ttk.Treeview):
    def __init__(self,master,columns):
        super().__init__(master,columns=columns,show="headings")
        for c in columns:
            self.heading(c,text=c)
            self.column(c,width=120,anchor="center")
