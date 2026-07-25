class BOQCategoryService:
    DEFAULT_CATEGORIES = [
        "Earthwork","Road Works","PCC","RCC","Brickwork",
        "Plaster","Steel","Pipe Culvert","Drainage","Finishing"
    ]

    def get_categories(self):
        return self.DEFAULT_CATEGORIES
