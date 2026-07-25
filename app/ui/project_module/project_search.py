import customtkinter as ctk

class ProjectSearch(ctk.CTkFrame):
    def __init__(self, master, on_search=None):
        super().__init__(master)
        self.entry=ctk.CTkEntry(self,placeholder_text="Search by code, project, client...")
        self.entry.pack(side="left",fill="x",expand=True,padx=(0,6))
        self.entry.bind("<KeyRelease>",lambda e:self.search(on_search))
        ctk.CTkButton(self,text="Search",width=90,
                      command=lambda:self.search(on_search)).pack(side="left")

    def search(self,callback):
        if callback:
            callback(self.entry.get())
