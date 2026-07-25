import customtkinter as ctk

class MaterialForm(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.fields={}
        for label in ("Code","Name","Unit","Rate"):
            ctk.CTkLabel(self,text=label).pack(anchor="w")
            e=ctk.CTkEntry(self)
            e.pack(fill="x",pady=2)
            self.fields[label.lower()]=e

    def get_data(self):
        return {
            "code": self.fields["code"].get(),
            "name": self.fields["name"].get(),
            "unit": self.fields["unit"].get(),
            "rate": float(self.fields["rate"].get() or 0)
        }

    def set_data(self,data):
        for k,v in data.items():
            if k in self.fields:
                self.fields[k].delete(0,"end")
                self.fields[k].insert(0,str(v))

    def clear(self):
        for e in self.fields.values():
            e.delete(0,"end")
