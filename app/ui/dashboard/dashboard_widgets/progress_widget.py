import customtkinter as ctk
from app.ui.components.card import Card

class ProgressWidget(Card):
    def __init__(self, master):
        super().__init__(master, title="Project Progress")
        self.bar = ctk.CTkProgressBar(self)
        self.bar.pack(fill="x", padx=10, pady=10)
        self.label = ctk.CTkLabel(self, text="0%")
        self.label.pack(pady=(0,10))
        self.set_progress(0)

    def set_progress(self, value):
        value = max(0, min(100, value))
        self.bar.set(value/100)
        self.label.configure(text=f"{value}%")
