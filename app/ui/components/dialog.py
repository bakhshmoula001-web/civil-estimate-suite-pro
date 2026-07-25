from tkinter import messagebox
class MessageDialog:
    @staticmethod
    def info(title,msg): messagebox.showinfo(title,msg)
    @staticmethod
    def warning(title,msg): messagebox.showwarning(title,msg)
    @staticmethod
    def error(title,msg): messagebox.showerror(title,msg)
