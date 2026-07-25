from app.ui.components.card import Card
import customtkinter as ctk

class SummaryWidget(Card):
    def __init__(self, master, title):
        super().__init__(master, title=title)
        self.value = ctk.CTkLabel(self, text="0", font=("Segoe UI",22,"bold"))
        self.value.pack(pady=10)

    def update(self, value):
        self.value.configure(text=str(value))
