import customtkinter as ctk

class ProjectPagination(ctk.CTkFrame):
    def __init__(self,master,on_prev=None,on_next=None):
        super().__init__(master)
        self.page=1
        ctk.CTkButton(self,text="<",width=40,command=on_prev).pack(side="left")
        self.label=ctk.CTkLabel(self,text="Page 1")
        self.label.pack(side="left",padx=8)
        ctk.CTkButton(self,text=">",width=40,command=on_next).pack(side="left")

    def set_page(self,page):
        self.page=page
        self.label.configure(text=f"Page {page}")
