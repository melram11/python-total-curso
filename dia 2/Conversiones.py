num1 = 20
num2 = 30.5

num1 = num1 + num2 # variable inplicita porque python la hizo automaticamente

print(num1)
print(type(num1))
print(type(num2))


# conversion explicita

num3 = 5.8
print(num3)
print(type(num3))

num4 = int(num3) # conversion explicita
print(num4)
print(type(num4))

edad = input("dime tu edad: ")
print(type(edad))
edad = int(edad) 

print(type(edad))
nueva_edad = 1 + edad
print(nueva_edad)

num5 = "7.5"
num6 = "10"

print(float(num6) + float(num5)) # concatenacion de strings
print('Hola ' + input("Dime tu nombre:") + " " + input("dime tu apellido:") +  "\nBuenos dias!" )


