import customtkinter as ctk

class Footer(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master,height=28)
        self.pack_propagate(False)
        self.status=ctk.CTkLabel(self,text="Ready",anchor="w")
        self.status.pack(side="left",padx=10)

    def set_status(self,text):
        self.status.configure(text=text)
