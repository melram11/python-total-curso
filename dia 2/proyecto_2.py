nombre = input("Cual es tu nombre:? ")
ventas = int(input("Cuantas has vendido este mes? "))
#comision = round(ventas * 13/100, 2) otra forma y la que pense de hacerlo 



#version funcional pero no mi version
comision = ventas * 13/100
print("Hola " + nombre + " tu comision de este mes sera de " + str(round(comision, 2)))


#mi version
nombre = input("Cual es tu nombre:? ")
ventas = int(input("Cuantas has vendido este mes? "))
comision = round(ventas * 13/100, 2)
print("Hola " + nombre + " tu comision de este mes sera de " + "$" + str((comision)))
#con formateo de cadenas
print("Hola " f"{nombre}, tu comisiones de este mes son ${comision}")
