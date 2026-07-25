import customtkinter as ctk
class Card(ctk.CTkFrame):
    def __init__(self,master,title="",**kw):
        super().__init__(master,corner_radius=10,**kw)
        ctk.CTkLabel(self,text=title,font=("Segoe UI",16,"bold")).pack(anchor="w",padx=10,pady=(8,4))
