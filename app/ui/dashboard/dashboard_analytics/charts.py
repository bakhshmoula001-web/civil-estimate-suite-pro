import customtkinter as ctk

class ChartPlaceholder(ctk.CTkFrame):
    def __init__(self, master, title):
        super().__init__(master)
        ctk.CTkLabel(self,text=title,font=("Segoe UI",16,"bold")).pack(pady=(10,5))
        self.canvas=ctk.CTkCanvas(self,height=220,bg="white",highlightthickness=1)
        self.canvas.pack(fill="both",expand=True,padx=10,pady=10)

    def draw_bar_chart(self,labels,values):
        self.canvas.delete("all")
        if not values:
            return
        w,h=700,220
        self.canvas.config(width=w,height=h)
        m=max(values) or 1
        bw=max(20,(w-40)//max(len(values),1)-10)
        x=20
        for lbl,val in zip(labels,values):
            bh=(val/m)*160
            self.canvas.create_rectangle(x,h-20-bh,x+bw,h-20)
            self.canvas.create_text(x+bw/2,h-8,text=lbl,font=("Arial",8))
            self.canvas.create_text(x+bw/2,h-30-bh,text=str(val),font=("Arial",8))
            x+=bw+10

    def draw_pie_placeholder(self,data):
        self.canvas.delete("all")
        self.canvas.create_oval(120,20,320,220)
        y=30
        for k,v in data.items():
            self.canvas.create_text(420,y,anchor="w",text=f"{k}: {v}")
            y+=20
