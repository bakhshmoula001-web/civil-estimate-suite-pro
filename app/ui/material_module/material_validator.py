class MaterialValidator:
    @staticmethod
    def validate(data):
        if not data["code"].strip():
            raise ValueError("Material code is required")
        if not data["name"].strip():
            raise ValueError("Material name is required")
        if data["rate"] < 0:
            raise ValueError("Rate cannot be negative")
        return True
