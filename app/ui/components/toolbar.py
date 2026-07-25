import customtkinter as ctk
class Toolbar(ctk.CTkFrame):
    def add_button(self,text,command=None):
        b=ctk.CTkButton(self,text=text,command=command,width=90)
        b.pack(side="left",padx=4,pady=4)
        return b
