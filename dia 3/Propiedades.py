
# no se puede modificar una cadena
#nombre = "Carina"
#nombre[0] = "k"
#print(nombre)

n1 = "Kari"
n2 = "na"
print(n1 + n2)
print(n1 * 10)


poema = """Mil pequeños peces blancosn 
conosi hirvieran
el color del agua""" # se puede usar triple comilla para escribir varias lineas
print(poema)
print("agua" in poema) # in busca una subcadena en la cadena
print("agua" not in poema) # not in busca una subcadena en la cadena
print("sol" in poema) # in busca una subcadena en la cadena
print("sol" not in poema) # not in busca una subcadena en la cadena

print(len(poema)) # len() devuelve la longitud de la cadena

hola = "Hola"
print(len(hola))

# ejercicios
#Práctica Propiedades de Strings 1
#Concatena 15 veces el texto "Repetición" y muestra el resultado en pantalla. Por suerte, conoces que los strings son multiplicables y puedes realizar esta actividad de forma simple y elegante.

rep = "Repetición"
print(rep * 15)


#Práctica Propiedades de Strings 2
#Verifica si la palabra "agua" no se encuentra en el siguiente haiku. Debes imprimir el booleano.
#Tierra mojada,
#mis recuerdos de viaje
#entre las lluvias

haiku = """Tierra mojada
mis recuerdos de viaje,
entre las lluvias"""
print("agua" not in haiku)


#Práctica Propiedades de Strings 3
#Muestra en pantalla el largo (en números de caracteres) de la palabra electroencefalografista.
numero_letras = "electroencefalografista"
print(len(numero_letras))