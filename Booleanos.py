var1 = True
var2 = False
print(type(var1))
print(var1)

numero = 5 > 2+3
print(type(numero))
print(numero)

numero = 5 == 2+3
print(type(numero))
print(numero)

numero = 5 >= 2+3
print(type(numero))
print(numero)

numero = 5 != 2+3
print(type(numero))
print(numero)

numero = bool(5>6)
print(type(numero))
print(numero)

numero = bool(5<6)
print(numero)
print(type(numero))

numero = bool() #FALSE
print(numero)
print(type(numero))

lista = [1,2,3,4]
control = 5 in lista
print(control)
print(type(control))

lista = [1,2,3,4]
control = 5 not in lista
print(control)
print(type(control))

# Práctica Booleanos 1
# Realiza una comparación que arroje como resultado un booleano
# y almacena el resultado (True/False) en una variable llamada prueba

prueba = 5 > 9
print (prueba)

# Práctica Booleanos 2
# Verifica si 17834/34 es mayor que 87*56 y
# muestra el resultado (booleano) en pantalla utilizando print()

print(17834/34 > 87*56)

# Práctica Booleanos 3
# Verifica si la raíz cuadrada de 25 es igual a 5
# y muestra el resultado (booleano) en pantalla utilizando print()

import math
raiz = math.sqrt(25) == 5
print(raiz)
#comentario actualizacion
