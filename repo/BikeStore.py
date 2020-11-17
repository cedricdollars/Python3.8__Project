class BikeStore:

    def __init__(self, stock=30):
        self.stock = stock

    def display_bike(self):
        print("We have {} bikes in the store".format(self.stock))
        return self.stock

    def display_available_bike(self):
        pass
