import customtkinter as ctk

class BOQForm(ctk.CTkFrame):
    def __init__(self,master,on_calculate=None,on_save=None):
        super().__init__(master)
        self.on_calculate=on_calculate
        self.on_save=on_save
        self.entries={}
        for lbl in ["Item Code","Description","Unit","Quantity","Rate"]:
            ctk.CTkLabel(self,text=lbl).pack(anchor="w")
            e=ctk.CTkEntry(self)
            e.pack(fill="x",pady=2)
            self.entries[lbl]=e
        self.amount=ctk.CTkLabel(self,text="Amount: 0.00")
        self.amount.pack(pady=6)
        ctk.CTkButton(self,text="Calculate",command=self.calculate).pack(side="left",padx=5)
        ctk.CTkButton(self,text="Save",command=self.save).pack(side="left")
    def calculate(self):
        q=float(self.entries["Quantity"].get() or 0)
        r=float(self.entries["Rate"].get() or 0)
        amt=q*r
        self.amount.configure(text=f"Amount: {amt:,.2f}")
        if self.on_calculate: self.on_calculate(amt)
    def save(self):
        if self.on_save: self.on_save()
