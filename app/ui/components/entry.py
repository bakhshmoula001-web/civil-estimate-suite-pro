import customtkinter as ctk
class AppEntry(ctk.CTkEntry):
    def __init__(self,master,placeholder="",**kw):
        super().__init__(master,placeholder_text=placeholder,**kw)
