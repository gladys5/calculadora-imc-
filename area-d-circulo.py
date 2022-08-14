# calcula el radio de un circulo y el area
from math import pi
diametro =  float(input('porfavor ingrese el diametro: '))

radio = diametro / 2

# radio = float(input('porfavor ingrese el radio del circulo: '))


area = pi * radio ** 2
print('el area del circulo es {}'.format(area))

