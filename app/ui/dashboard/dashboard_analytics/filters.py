import customtkinter as ctk

class DateFilter(ctk.CTkFrame):
    def __init__(self,master,callback=None):
        super().__init__(master)
        self.start=ctk.CTkEntry(self,placeholder_text="Start Date")
        self.end=ctk.CTkEntry(self,placeholder_text="End Date")
        self.start.pack(side="left",padx=5)
        self.end.pack(side="left",padx=5)
        ctk.CTkButton(self,text="Apply",
            command=lambda: callback(self.start.get(),self.end.get()) if callback else None).pack(side="left",padx=5)
