#Input se utiliza para que el usuario introduzca un dato
valor = input("Ingrese un número: ")
print(valor + ' es el número que has ingresado')

#Para realizar una operacion con el numero ingresado por el usuario, debo de convertir esa cadena a numero, colocando la palabra "int" 
print('Cuando multiplique el número por 10, el resultado es: ')
valor_int = int(valor)
print(valor_int * 10)