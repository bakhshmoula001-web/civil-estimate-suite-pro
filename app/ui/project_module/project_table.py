import tkinter as tk
from tkinter import ttk

class ProjectTable(ttk.Frame):
    COLUMNS=(
        "ID","Code","Project","Client",
        "Location","Status","Start Date","End Date"
    )

    def __init__(self,master,on_double_click=None):
        super().__init__(master)
        self.on_double_click=on_double_click
        self._sort_reverse={}

        self.tree=ttk.Treeview(
            self,
            columns=self.COLUMNS,
            show="headings",
            selectmode="browse"
        )

        vs=ttk.Scrollbar(self,orient="vertical",command=self.tree.yview)
        hs=ttk.Scrollbar(self,orient="horizontal",command=self.tree.xview)

        self.tree.configure(yscrollcommand=vs.set,xscrollcommand=hs.set)

        self.tree.grid(row=0,column=0,sticky="nsew")
        vs.grid(row=0,column=1,sticky="ns")
        hs.grid(row=1,column=0,sticky="ew")

        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0,weight=1)

        for col in self.COLUMNS:
            self.tree.heading(
                col,
                text=col,
                command=lambda c=col:self.sort_by(c)
            )
            self.tree.column(col,width=140,anchor="center")

        self.tree.bind("<Double-1>",self._double_click)

    def load(self,projects):
        self.clear()
        for p in projects:
            self.tree.insert(
                "",
                "end",
                values=(
                    getattr(p,"id",""),
                    getattr(p,"project_code",""),
                    getattr(p,"project_name",""),
                    getattr(p,"client_name",""),
                    getattr(p,"location",""),
                    getattr(p,"status",""),
                    getattr(p,"start_date",""),
                    getattr(p,"end_date","")
                )
            )

    def clear(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

    def selected(self):
        item=self.tree.focus()
        if not item:
            return None
        return self.tree.item(item)["values"]

    def delete_selected(self):
        item=self.tree.focus()
        if item:
            self.tree.delete(item)

    def refresh(self,projects):
        self.load(projects)

    def sort_by(self,column):
        data=[(self.tree.set(k,column),k) for k in self.tree.get_children("")]
        reverse=self._sort_reverse.get(column,False)
        data.sort(reverse=reverse)
        for index,(_,k) in enumerate(data):
            self.tree.move(k,"",index)
        self._sort_reverse[column]=not reverse

    def _double_click(self,event):
        if self.on_double_click:
            row=self.selected()
            if row:
                self.on_double_click(row)
