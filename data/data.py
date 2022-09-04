from Employe import Employe
from Client import Client


emp = Employe('Gladys', 'Yomaira', '4754', '6563392584', 1000)
cli = Client('Rufino', 'Parra', '17457', '6561234567', 'vip')


def load():
    response = input(' you need add  a new employee? ')
    name = input('add name ')
    lastname = input('add lastname ')
    dni = input('add dni ')
    phone = input('add phone')

    if (response == 'yes'):
        salary = input('add salary')
        emp = Employe(name, lastname, dni, phone, int(salary))
        persons.append(emp)
    else:
        type = input('add type of client ')
        cli = Client(name, lastname, dni, phone, type)
        persons.append(cli)

persons = []

load()

for person in persons:
    print(person)