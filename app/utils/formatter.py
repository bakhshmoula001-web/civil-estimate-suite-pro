from datetime import datetime

class Formatter:
    @staticmethod
    def currency(value):
        return f"PKR {value:,.2f}"

    @staticmethod
    def quantity(value):
        return f"{value:,.3f}"

    @staticmethod
    def date(value=None):
        if value is None:
            value = datetime.now()
        return value.strftime("%d-%m-%Y")
