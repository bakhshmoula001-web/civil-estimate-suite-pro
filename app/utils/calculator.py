class Calculator:
    @staticmethod
    def amount(quantity: float, rate: float) -> float:
        return round(quantity * rate, 2)

    @staticmethod
    def percentage(value: float, total: float) -> float:
        return 0 if total == 0 else round((value / total) * 100, 2)

    @staticmethod
    def volume(length, width, height):
        return round(length * width * height, 3)

    @staticmethod
    def area(length, width):
        return round(length * width, 3)
