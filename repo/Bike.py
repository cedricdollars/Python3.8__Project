class Bike:
    def __init__(self, model: str, price: int, isAvailable: bool):
        self.model = model
        self.price = price
        self.isAvailable = isAvailable

    def get_model(self):
        return self.model

    def get_price(self):
        return self.price

    def set_model(self, model):
        self.model = model

    def set_price(self, price):
        self.price = price
