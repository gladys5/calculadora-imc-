from Person import Person


class Employe(Person):
    def __init__(self, name, lastname, dni, phone, salary):
        super().__init__(name, lastname, dni, phone)
        self.salary = salary
