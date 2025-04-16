my_tuple = (1,2,(10,20),4)
#t = (5,5.6,"ff")
print(type(my_tuple))
print(my_tuple[0])
print(my_tuple[-2])
print(my_tuple[2][0])

#casting
my_tuple = list(my_tuple)

print(my_tuple[0])

print(type(my_tuple))

t = (1,2,3)

x,y,z = t
print(x,y,z)

y = (1,2,3,1)

print(y.count(1))
print(y.index(2))

#ejercicio

# Práctica Tuples 1
# Utiliza un método de tuplas para contar la cantidad de veces que aparece el valor 2
# en la siguiente tupla, y muestra el resultado (integer) en pantalla:
# mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
print(mi_tupla.count(2))


#
#Práctica Tuples 2
#Convierte a lista la siguiente tupla, y almacénala en una variable llamada mi_lista.

#mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
mi_tupla = list(mi_tupla)
mi_lista = mi_tupla

#Práctica Tuples 3
#Extrae los elementos de la siguiente tupla en cuatro variables: a, b, c, d
#mi_tupla = (1, 2, 3, 4)

mi_tupla = (1, 2, 3, 4)

a,b,c,d = mi_tupla
print(a,b,c,d)