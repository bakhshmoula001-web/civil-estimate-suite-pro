import customtkinter as ctk
class PrimaryButton(ctk.CTkButton):
    def __init__(self,master,text,command=None,**kw):
        super().__init__(master,text=text,command=command,corner_radius=8,**kw)
