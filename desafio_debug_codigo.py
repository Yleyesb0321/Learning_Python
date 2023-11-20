#El codigo debe de recomendar un tipo de planta segun el cuidado que requiera la planta (bajo, medio o alto)
#Pistas: hay errores de sitaxis, de ejecucion y de logica
def planta (cuidado):
  if cuidado == 'bajo': #Error sintaxis, se debe comparar los valores con doble =
    print('Suculenta')
  elif cuidado == 'medio':
    print('Pothos')
  elif cuidado == 'alto': #Aqui hay error de logica, cambiar 'medio' por 'alto'
    print('Orquidea')
    
#Se llama a la funcion
planta ('bajo')
planta ('medio')
planta ('alto')