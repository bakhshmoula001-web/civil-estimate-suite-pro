import customtkinter as ctk
from app.ui.components.entry import AppEntry
from app.ui.components.combobox import AppComboBox
from app.ui.components.button import PrimaryButton
from app.utils.validators import Validator

STATUS=["Planning","Running","Completed","On Hold","Cancelled"]

class ProjectForm(ctk.CTkFrame):
    def __init__(self,master,on_save=None):
        super().__init__(master)
        self.on_save=on_save
        self.inputs={}
        self._build()

    def _row(self,parent,label,key,combo=False,values=None):
        ctk.CTkLabel(parent,text=label).pack(anchor="w",padx=5)
        w=AppComboBox(parent,values=values) if combo else AppEntry(parent,placeholder=label)
        w.pack(fill="x",padx=5,pady=(0,8))
        self.inputs[key]=w

    def _build(self):
        left=ctk.CTkFrame(self)
        right=ctk.CTkFrame(self)
        left.pack(side="left",fill="both",expand=True,padx=10,pady=10)
        right.pack(side="left",fill="both",expand=True,padx=10,pady=10)

        self._row(left,"Project Code","project_code")
        self._row(left,"Project Name","project_name")
        self._row(left,"Client","client_name")
        self._row(left,"Consultant","consultant")
        self._row(left,"Contractor","contractor")

        self._row(right,"Location","location")
        self._row(right,"Start Date (YYYY-MM-DD)","start_date")
        self._row(right,"End Date (YYYY-MM-DD)","end_date")
        self._row(right,"Status","status",True,STATUS)

        ctk.CTkLabel(right,text="Remarks").pack(anchor="w",padx=5)
        self.remarks=ctk.CTkTextbox(right,height=120)
        self.remarks.pack(fill="x",padx=5,pady=(0,8))

        bar=ctk.CTkFrame(self,fg_color="transparent")
        bar.pack(fill="x",padx=10,pady=10)
        PrimaryButton(bar,text="Save",command=self.save).pack(side="right",padx=5)
        PrimaryButton(bar,text="Clear",command=self.clear).pack(side="right",padx=5)

    def data(self):
        d={}
        for k,w in self.inputs.items():
            d[k]=w.get()
        d["remarks"]=self.remarks.get("1.0","end").strip()
        return d

    def validate(self):
        d=self.data()
        Validator.required(d["project_code"],"Project Code")
        Validator.required(d["project_name"],"Project Name")
        Validator.required(d["client_name"],"Client")
        return d

    def save(self):
        data=self.validate()
        if self.on_save:
            self.on_save(data)

    def clear(self):
        for w in self.inputs.values():
            w.delete(0,"end")
        self.remarks.delete("1.0","end")
