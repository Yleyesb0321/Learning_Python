#Vamos a crear un programa que nos cambie las letras minusculas en mayusculas
primer_nombre = 'cristina'
segundo_nombre = 'hurtado'
nota = 'Ganadora del Premio de la academia de Actores'

#Para realizar el cambio de la primera letra en minusculas a mayusculas utilizamos la funcion "capitalize"

primer_nombre_cap = primer_nombre.capitalize()
segundo_nombre_cap = segundo_nombre.capitalize()

print(primer_nombre_cap)
print(segundo_nombre_cap)

#Para buscar dentro de una cadena utilizamos "find" y dentro colocamos la palabra a buscar, nos arrojara la posicion del indice donde se encuentra la palabra
premio_ubicacion = nota.find('Premio')
print(premio_ubicacion)

#Para sustraer una cadena dentro de otra cadena, colocando los corchetes [] e indicandole el número del indice donde inicia el texto que queremos encontrar, seguido de 2 puntos ":" y dejandolo en blanco, para que nos llame hasta el final del texto 
premio_text = nota[13:]
print(premio_text)