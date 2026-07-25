from datetime import datetime

class Helpers:
    @staticmethod
    def today():
        return datetime.today().strftime("%Y-%m-%d")

    @staticmethod
    def now():
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def safe_float(value, default=0.0):
        try:
            return float(value)
        except Exception:
            return default
