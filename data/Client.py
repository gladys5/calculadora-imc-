from Person import Person


class Client(Person):
    def __init__(self, name, lastname, dni, phone, category):
        super().__init__(name, lastname, dni, phone)
        self.category = category