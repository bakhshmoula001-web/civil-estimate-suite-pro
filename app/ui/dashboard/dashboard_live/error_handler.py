import logging
from tkinter import messagebox

class DashboardErrorHandler:
    @staticmethod
    def handle(exc):
        logging.exception(exc)
        messagebox.showerror(
            "Dashboard Error",
            str(exc)
        )
