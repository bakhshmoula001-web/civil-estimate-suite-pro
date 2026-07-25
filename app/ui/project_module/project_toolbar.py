import customtkinter as ctk

class ProjectToolbar(ctk.CTkFrame):
    def __init__(self, master, callbacks=None):
        super().__init__(master)
        callbacks = callbacks or {}
        actions=[
            ("New","new"),("Edit","edit"),("Delete","delete"),
            ("Refresh","refresh"),("Export Excel","excel"),
            ("Export PDF","pdf")
        ]
        for text,key in actions:
            ctk.CTkButton(
                self,text=text,width=110,
                command=callbacks.get(key)
            ).pack(side="left",padx=4,pady=6)
