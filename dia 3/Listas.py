mi_lista = ['a', 'b', 'c']
mi_lista2 =['d', 'e', 'f']
mi_lista3 = mi_lista + mi_lista2
resultado = (mi_lista)
print(len(resultado))
print(resultado[0:2]) #imprime los elementos de la posicion 0 a la 2
print(mi_lista + mi_lista2)
mi_lista3[0] = 'pollo' #cambia el valor de la posicion 0
mi_lista3.append('g') #agrega un elemento al final de la lista
mi_lista3.pop() #elimina el ultimo elemento de la lista
mi_lista3.pop(1) #elimina el elemento de la posicion 1
elimindado = mi_lista3.pop(3) #elimina el elemento de la posicion 4 y lo guarda en la variable eliminado
print(mi_lista3)
print(elimindado)

lista = ['c','s','d','g','a']
lista2 = [1,2,3,4,5]
lista.sort() #ordena la lista
lista2.reverse() #invierte la lista
print(lista)
print(lista2)

#ejericios

#Práctica Listas 1
#Crea una lista con 5 elementos, dentro de la variable mi_lista. Puedes incluir strings, booleanos, números, etc.

mi_lista = [1,'a','s',3,"false"]

#Práctica Listas 2
#Agrega el elemento "motocicleta" a la siguiente lista de medios de transporte:
#medios_transporte = ["avión", "auto", "barco", "bicicleta"]
#No debes modificar la línea de código ya suministrada, sino que debes emplear el método apropiado de listas para añadir un nuevo elemento.

medios_transporte = ["avión", "auto", "barco", "bicicleta"]
medios_transporte.append("motocicleta")
print(medios_transporte)


#Práctica Listas 3
#Utiliza el método pop() para quitar el tercer elemento de la siguiente lista llamada frutas, y almacénalo en una variable llamada eliminado. Utiliza métodos de listas sin alterar la línea de código ya suministrada.
#manzana
#banana
#mango
#cereza
#sandía

frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
eliminada = frutas.pop(2)
print(frutas)
print(eliminada)
