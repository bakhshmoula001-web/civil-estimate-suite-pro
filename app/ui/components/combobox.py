import customtkinter as ctk
class AppComboBox(ctk.CTkComboBox):
    def __init__(self,master,values=None,**kw):
        super().__init__(master,values=values or [],**kw)
