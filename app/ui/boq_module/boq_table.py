from tkinter import ttk
class BOQTable(ttk.Frame):
    COLS=("Code","Description","Unit","Qty","Rate","Amount")
    def __init__(self,master):
        super().__init__(master)
        self.tree=ttk.Treeview(self,columns=self.COLS,show="headings")
        for c in self.COLS:
            self.tree.heading(c,text=c)
            self.tree.column(c,width=120)
        self.tree.pack(fill="both",expand=True)
    def load(self,rows):
        for i in self.tree.get_children(): self.tree.delete(i)
        for r in rows: self.tree.insert("", "end", values=r)
