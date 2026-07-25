class Validator:
    @staticmethod
    def required(value, field):
        if value is None or str(value).strip() == "":
            raise ValueError(f"{field} is required.")
        return True

    @staticmethod
    def positive(value, field):
        if float(value) < 0:
            raise ValueError(f"{field} must be positive.")
        return True

    @staticmethod
    def number(value, field):
        try:
            float(value)
            return True
        except Exception:
            raise ValueError(f"{field} must be numeric.")
