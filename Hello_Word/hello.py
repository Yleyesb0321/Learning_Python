print("Hola Houston....!")

#program
sum = 1 + 2 #=3
product = sum * 2
print(product)

#Tipos de Datos
planets_in_solar_system = 8 # int, pluto used to be the 9th planet, but is too small
distance_to_alpha_centauri = 4.367 # float, lightyears
can_liftoff = True
shuttle_landed_on_the_moon = "Apollo 11" #string

#Para saber el tipo de datos se utiliza type()
type(distance_to_alpha_centauri) ## <class 'float'>

#Operadores Basicos
#suma +
#resta -
#Multiplicacion *
#Division /
left_side = 10
right_side = 5
left_side / right_side # 2

#Operadores de asignacion
# = igual
# += mas o igual
# -= menos o igual
# /= entre o igual
#= *= por o igual

#Fechas
#Para trabajar con una fecha, debe importar el módulo date:
from datetime import date
date.today() #se llama la funcion de la fecha, today()
print(date.today())

#Conversión de tipos de datos
#Para convertir un dato en texto se utiliza la funcion str()
print("Today's date is: " + str(date.today()))

#Entrada de usuarios por consola se usa input()
print("Welcome to the greeter program")
name = input("Enter your name: ")
print("Greetings " + name)

#Para convertir cadenas a numeros se usa int()
print("calculator program")
first_number = input("first number: ")
second_number = input("second number: ")
print(int(first_number) + int(second_number))

#Ejemplo
parsecs_input = input("Input numbers of parsecs:")
parsecs = int(parsecs_input)
lightyears = 3.26156 * parsecs

print(parsecs_input + " parsecs is " + str(lightyears) + " lightyears")

