import customtkinter as ctk
from app.ui.components.card import Card

class RecentActivitiesWidget(Card):
    def __init__(self, master):
        super().__init__(master, title="Recent Activities")
        self.box = ctk.CTkTextbox(self, height=250)
        self.box.pack(fill="both", expand=True, padx=10, pady=10)

    def load(self, activities):
        self.box.delete("1.0","end")
        for item in activities:
            self.box.insert("end", f"• {item}\n")
