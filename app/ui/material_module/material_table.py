from tkinter import ttk

class MaterialTable(ttk.Frame):
    COLS=("ID","Code","Name","Unit","Rate")
    def __init__(self,master):
        super().__init__(master)
        self.tree=ttk.Treeview(self,columns=self.COLS,show="headings")
        for c in self.COLS:
            self.tree.heading(c,text=c)
            self.tree.column(c,width=120)
        self.tree.pack(fill="both",expand=True)

    def load(self,rows):
        self.clear()
        for r in rows:
            self.tree.insert("","end",values=r)

    def selected(self):
        item=self.tree.focus()
        return self.tree.item(item)["values"] if item else None

    def clear(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
