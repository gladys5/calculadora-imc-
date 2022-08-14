#calculadora imc

peso = int(input('Ingrese su peso en kg'))
alturaEnCM = int(input('Ingrese su altura en cm'))
alturaEnMetros = alturaEnCM / 100
imc = peso / (alturaEnMetros * alturaEnMetros)

print('Su IMC es de ' + str(imc))

if imc < 20:
    print('Estado de delgadez')
if imc >= 20 and imc < 26:
    print('Peso normal')
if imc >= 26 and imc < 30:
    print('Estado de sobrepeso')
if imc >= 30:
    print('Estado de obesidad')


