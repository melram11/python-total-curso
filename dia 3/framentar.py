texto = "ABCDEFGHIJKLM"
fragmento = texto[2:5]
print(fragmento)

texto = "ABCDEFGHIJKLM"
fragmento = texto[2:] # si no se pone el segundo valor, se toma hasta el final
print(fragmento)


texto = "ABCDEFGHIJKLM"
fragmento = texto[:5] # si no se pone el primer valor, se toma desde el principio
print(fragmento)

texto = "ABCDEFGHIJKLM"
fragmento = texto[2:10:2] # el tercer valor es el salto
print(fragmento)

texto = "ABCDEFGHIJKLM"
fragmento = texto[::3]
print(fragmento)

texto = "ABCDEFGHIJKLM"
fragmento = texto[::-2] # si el salto es negativo, se toma de derecha a izquierda
print(fragmento)

# ejercicios

# Práctica Sub-Strings 1
# Extrae la primera palabra de la siguiente frase utilizando slicing, y muéstrala en pantalla:
# "Controlar la complejidad es la esencia de la programación"
# Pista: "Controlar" tiene un largo de 9 caracteres.

frase = "Controlar la complejidad es la esencia de la programación"
fragmento = frase[0:9]
print(fragmento)

# Práctica Sub-Strings 2 
# Toma cada tercer caracter empezando desde el noveno hasta el final de la frase, e imprime el resultado.
# "Nunca confíes en un ordenador que no puedas lanzar por una ventana"

frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
fragmento = frase[8::3]
print(fragmento)

# Práctica Sub-Strings 3
# Invierte la posición de todos los caracteres de la siguiente frase y muestra el resultado en pantalla.
# "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"

frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
fragmentar = frase[::-1] #comun para invertir valores
print(fragmentar)