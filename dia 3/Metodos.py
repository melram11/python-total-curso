# uppe() convierte todo el texto en mayúsculas     
texto = "Este es el texto de Federico"

resultado = texto.upper()

print(resultado) 


texto = "Este es el texto de Federico"

resultado = texto[2].upper() # el tercer caracter de la cadena se convierte en mayúscula

print(resultado) 

# lower() convierte todo el texto en minúsculas
texto = "Este es el texto de Federico"

resultado = texto.lower()

print(resultado) 

#split() divide la cadena en subcadenas

texto = "Este es el texto de Federico"

resultado = texto.split()

print(resultado) 

texto = "Este es el texto de Federico"

resultado = texto.split("t")

print(resultado) 

#join() une las subcadenas

a = "Aprender"
b = "Python"
c = "es"
d = "fantástico"
e = " ".join([a, b, c, d])
print(e)

a = "Aprender"
b = "Python"
c = "es"
d = "fantástico"
e = "-".join([a, b, c, d])
print(e)

#find() busca una subcadena en la cadena
texto = "Este es el texto de Federico"
resultado = texto.find("g")

print(resultado)

texto = "Este es el texto de Federico"
resultado = texto.find("texto")

print(resultado)

#replace() reemplaza una subcadena por otra

texto = "Este es el texto de Federico"
resultado = texto.replace("Federico", "Juan") 

print(resultado)

#ejericios

#Práctica Métodos de String 1
#Imprime el siguiente texto en mayúsculas, empleando el método específico de strings:

frase = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."

print(frase.upper())


#Práctica Métodos de String 2
#Une la siguiente lista en un string, separando cada elemento con un espacio. Utiliza el método apropiado de listas/strings, y muestra en pantalla el resultado.

lista_palabras = ["La","legibilidad","cuenta."]

palabra = " ".join(["La","legibilidad","cuenta."]) 
print(palabra)


#Práctica Métodos de String 3
#Reemplaza en la siguiente frase:
#"Si la implementación es difícil de explicar, puede que sea una mala idea."
#los siguientes pares de palabras:
#"difícil" --> "fácil"
#"mala" --> "buena"
#y muestra en pantalla la frase con ambas palabras modificadas.

frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."

frase = frase.replace("difícil", "fácil")
frase = frase.replace("mala", "buena")
print(frase)