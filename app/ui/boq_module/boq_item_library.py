DEFAULT_ITEMS = {
    "PCC":[
        {"code":"PCC-001","description":"Plain Cement Concrete 1:2:4","unit":"Cft","rate":0},
        {"code":"PCC-002","description":"Lean Concrete","unit":"Cft","rate":0}
    ],
    "Brickwork":[
        {"code":"BRK-001","description":"Brick Masonry in CM","unit":"Cft","rate":0}
    ],
    "Earthwork":[
        {"code":"EAR-001","description":"Excavation in Ordinary Soil","unit":"Cft","rate":0}
    ]
}

class BOQItemLibrary:
    def categories(self):
        return list(DEFAULT_ITEMS.keys())

    def items(self, category):
        return DEFAULT_ITEMS.get(category, [])

    def get_item(self, category, code):
        for item in self.items(category):
            if item["code"] == code:
                return item
        return None
