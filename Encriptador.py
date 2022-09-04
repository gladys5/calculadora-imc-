#CREANDO UN ARCHIVO
# archivo = open('texto.txt', 'a')
# archivo.write('prueba de guardado en el archivo')
# archivo.close()

# LEEMOS EL CONTENIDO DEL ARCHIVO CREADO
# archivo = open('texto.txt', 'r')
# print(archivo.read())


#ENCRIPTAR ARCHIVO CREADO
def encriptar(texto):
    textoFinal = ''
    for letra in texto:
        caracter = ord(letra)
        caracter += 1
        textoFinal += chr(caracter)
    return textoFinal


#DESENCRIPTAR  ARCHIVO
def desencriptar(texto):
    print('texto a desencriptar: ' + texto)
    textoFinal = ''
    for letra in texto:
        caracter = ord(letra)
        caracter -= 1
        textoFinal += chr(caracter)
    return textoFinal

def encriptarArchivo(rutaArchivo):
    archivo = open(rutaArchivo, 'r')
    texto = archivo.read()
    archivo.close()
    textoEncriptado = encriptar(texto)

    archivo = open(rutaArchivo, 'w')
    archivo.write(textoEncriptado)
    archivo.close()
    print('el archivo se encripto correctamente')



def desencriptarArchivo(rutaArchivo):
    archivo = open(rutaArchivo, 'r')
    texto = archivo.read()
    archivo.close()
    textoDesencriptado = desencriptar(texto)

    archivo = open(rutaArchivo, 'w')
    archivo.write(textoDesencriptado)
    archivo.close()



respuestaEoD = input('presione "E" para encriptar, o "D" para desencriptar')
rutaArchivo = input('ingrese la ruta del archivo')

if respuestaEoD == 'E':
    encriptarArchivo(rutaArchivo)
else:
    desencriptarArchivo(rutaArchivo)
