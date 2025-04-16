diccionario = {'c1': 'valor1', 'c2': 'valor2'} # los valores se puede repetir, las clavas no
print(diccionario)

resultado = diccionario['c1']
print(resultado)

cliente = {"nombre":" Juan", "apellido" : "Fuentes", "peso": 70, " talla" : 1.76}
consulta = cliente["apellido"]
print(consulta)

consulta = cliente["nombre"]
print(consulta)

dic = {'cs1':55, 'cs2':[10,20,30], 'cs3':{'s1': 100, 's2':200}}
print(dic['cs2'])

dic = {'cs1':55, 'cs2':[10,20,30], 'cs3':{'s1': 100, 's2':200}}
print(dic['cs2'][1])

dic2 = {'z1':['a','b','c'], 'z2': ['d','e','f']}
print(dic2['z2'][1].upper())

dic3 = {1: 'a', 2:'b'}
print(dic3)

dic3[3] = 'c'
print(dic3)

dic3[2] = "B"
print(dic3)

print(dic3.keys())
print(dic3.values())
print(dic3.items())

# ejercicios

#Práctica Diccionarios 1
#Crea un diccionario llamado mi_dic que almacene la siguiente información de una persona:
#nombre: Karen
#apellido: Jurgens
#edad: 35
#ocupacion: Periodista
#Los nombres de las claves y valores deben ser iguales a la consigna..

#nombre: Karen
#apellido: Jurgens
#edad: 35
#ocupacion: Periodista

mi_dic = {'nombre': 'Karen' , 'apellido': 'Jurgens', 'edad': 35, 'ocupacion': 'Periodista'}

#ejerciocio 2

#Práctica Diccionarios 2
#Crea una función print que devuelva del segundo item de la lista llamada points2,
# dentro del siguiente diccionario.
#Si el valor 300 cambiara en el futuro,
# el código debería funcionar igual para devolver el valor que se encuentre en esa misma posición.
# Para ello, deberás hacer referencia a los nombres de las claves y/o índices según corresponda.

mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict['puntos']['points2'][1])

# Práctica Diccionarios 3
# Actualiza la información de nuestro diccionario llamado mi_dic
# (reasignando nuevos valores a las claves según corresponda),
# y agrega una nueva clave llamada "pais" (sin tilde). Los nuevos datos son:
# nombre: Karen
# apellido: Jurgens
# edad: 36
# ocupacion: Editora
# pais: Colombia
# para ello, no debes cambiar la línea de código ya escrita,
# sino actualizar los valores mediante métodos de diccionarios.

#mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}

mi_dic['ocupacion'] = 'Editora'
mi_dic['edad'] = 36
mi_dic['pais'] = 'Colombia'
print(mi_dic)