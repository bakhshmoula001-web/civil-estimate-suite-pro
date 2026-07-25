import customtkinter as ctk

STATUS=["All","Planning","Running","Completed","On Hold","Cancelled"]

class ProjectFilter(ctk.CTkFrame):
    def __init__(self,master,on_change=None):
        super().__init__(master)
        ctk.CTkLabel(self,text="Status").pack(side="left",padx=(0,5))
        self.combo=ctk.CTkComboBox(self,values=STATUS,
            command=lambda v:on_change(v) if on_change else None)
        self.combo.set("All")
        self.combo.pack(side="left")
