import customtkinter as ctk
class SearchBox(ctk.CTkFrame):
    def __init__(self,master,callback=None):
        super().__init__(master)
        self.entry=ctk.CTkEntry(self,placeholder_text="Search...")
        self.entry.pack(side="left",fill="x",expand=True)
        ctk.CTkButton(self,text="Search",width=80,
            command=lambda: callback(self.entry.get()) if callback else None).pack(side="left",padx=4)
