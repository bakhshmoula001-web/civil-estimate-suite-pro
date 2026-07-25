class BOQLibraryController:
    def __init__(self, library, form):
        self.library = library
        self.form = form

    def load_categories(self):
        return self.library.categories()

    def load_items(self, category):
        return self.library.items(category)

    def apply_item(self, category, code):
        item = self.library.get_item(category, code)
        if item:
            self.form.set_item_template(item)
        return item
