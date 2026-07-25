import customtkinter as ctk
from app.ui.components.card import Card
from app.ui.components.table import DataTable

class RecentProjectsWidget(Card):
    def __init__(self, master):
        super().__init__(master, title="Recent Projects")
        self.table = DataTable(self, ("Code","Project","Status"))
        self.table.pack(fill="both", expand=True, padx=10, pady=10)

    def load(self, rows):
        for i in self.table.get_children():
            self.table.delete(i)
        for row in rows:
            self.table.insert("", "end", values=row)
