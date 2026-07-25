import customtkinter as ctk

class Workspace(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.label=ctk.CTkLabel(self,text="Dashboard",
                                font=("Segoe UI",24,"bold"))
        self.label.pack(expand=True)

    def show(self,page):
        self.label.configure(text=page)
