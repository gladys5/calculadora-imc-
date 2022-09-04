class Person:
    def __init__(self, name, lastname, dni, phone):
        self.name = name
        self.lastName = lastname
        self.dni = dni
        self.phone = phone

    def __str__(self):
        return self.name + ' ' +  self.lastName + ' - ' + self.dni