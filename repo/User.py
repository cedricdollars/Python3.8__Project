class User:
    def __init__(self, email: str, fullname: str, password: str):
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.password = password

    def get_email(self):
        return self.email

    def get_fullname(self):
        return self.fullname

    def get_password(self):
        return self.password

    def set_email(self, email):
        self.email = email

    def set_fullname(self, fullname):
        self.fullname = fullname

    def set_password(self, password):
        self.password = password
