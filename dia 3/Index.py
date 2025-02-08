mi_texto = "Esta es una prueba"
resultado = mi_texto[0]
print(resultado)

mi_texto = "Esta es una prueba"
resultado = mi_texto[9]
print(resultado)

mi_texto = "Esta es una prueba"
resultado = mi_texto[-4]
print(resultado)

mi_texto = "Esta es una prueba"
resultado = mi_texto.index("n")
print(resultado)

mi_texto = "Esta es una prueba"
resultado = mi_texto.index("prueba")
print(resultado)

mi_texto = "Esta es una prueba"
resultado = mi_texto.index("a")
print(resultado)

mi_texto = "Esta es una prueba"
resultado = mi_texto.index("a", 5) # index busca de izquierda a derecha
print(resultado)

mi_texto = "Esta es una prueba"
resultado = mi_texto.rindex("a") # rindex busca de derecha a izquierda
print(resultado)


# ejercicios

#Práctica Método Index() 1
#Encuentra y muestra en pantalla
#qué caracter ocupa la quinta posición dentro de la siguiente palabra:
# "ordenador"

palabra = "ordenador"
resultado = palabra[4]
print(resultado)

#Práctica Método Index() 2 
# Encuentra y muestra en pantalla el índice de la primera aparición de la palabra "práctica" en la siguiente frase:
#"En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
resultado = frase.index("práctica")
print(resultado)

# Práctica Método Index() 3
# Encuentra y muestra en pantalla el índice de la última aparición de la palabra "práctica" en la siguiente frase:
# "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
resultado = frase.rindex("práctica")
print(resultado)