
import re

cod_cinco_digitos = '12345'
cod_nueve_digitos = '12345-6789'
num_tel = '123-456-7890'

#Para realizar la busqueda se coloca la funcion r, seguido de comillas simples, dentro de las '' colocamos la contra barra y la letra d, la cual nos indica que vamos a buscar numeros
regex_cinco_digitos = r'\d{5}'

#Para imprimir colocamos el archivo importado "re" seguido de un "." y la palabra search, esto nos pedira 2 parametros, primero colocamos la expresion regular y luego la cadena donde vamos a hacer la busqueda
print(re.search(regex_cinco_digitos, cod_cinco_digitos))
print(re.search(regex_cinco_digitos, cod_nueve_digitos))
print(re.search(regex_cinco_digitos, num_tel))