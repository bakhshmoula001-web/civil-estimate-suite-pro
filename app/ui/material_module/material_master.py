class MaterialMaster:
    DEFAULT=[
        {"code":"MAT-001","name":"Cement","unit":"Bag"},
        {"code":"MAT-002","name":"Sand","unit":"Cft"},
        {"code":"MAT-003","name":"Crush","unit":"Cft"},
        {"code":"MAT-004","name":"Steel","unit":"Kg"},
        {"code":"MAT-005","name":"Bricks","unit":"Nos"},
    ]
    def all(self):
        return self.DEFAULT
