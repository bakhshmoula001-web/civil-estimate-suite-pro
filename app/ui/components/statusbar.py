import customtkinter as ctk
class StatusBar(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master,height=28)
        self.label=ctk.CTkLabel(self,text="Ready")
        self.label.pack(side="left",padx=8)
    def set(self,msg):
        self.label.configure(text=msg)
