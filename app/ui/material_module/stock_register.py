class StockRegister:
    def __init__(self):
        self.stock={}
    def receipt(self,name,qty):
        self.stock[name]=self.stock.get(name,0)+float(qty)
    def issue(self,name,qty):
        self.stock[name]=self.stock.get(name,0)-float(qty)
    def balance(self):
        return dict(self.stock)
