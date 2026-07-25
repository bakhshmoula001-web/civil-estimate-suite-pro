import customtkinter as ctk
class Pagination(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        self.page=1
        self.label=ctk.CTkLabel(self,text="Page 1")
        self.label.pack(side="left",padx=6)
    def set_page(self,p):
        self.page=p
        self.label.configure(text=f"Page {p}")
