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
