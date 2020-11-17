class Customer:
    def __init__(self, firstname, lastname, email, password):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.bike_rental = 0

    def request_bike(self):
        bikes = input("Combien de vélos voulez vous ?")
        try:
            bikes = int(bikes)
        except ValueError:
            print("Valeur incorrect, réesaayer!")
        if bikes < 1:
            print("Vous devez effectuer une demande supérieur à 1")
            return -1
        if bikes > 5:
            print("Désolé, vous ne pouvez pas demander plus de 5 vélos")
            return -1
        else:
            cls.bike_rental = bikes
            return self.bike_rental
