#Agregando Valores del archivo txt, utilizando las entradas y salidas
archivoN = open('valores.txt', 'rt')
archivoS = open('valores_totales.txt', 'wt')
print('Procesando entrada')


suma = 0

for linea in archivoN:
  suma += int(linea)
  print(linea.rstrip(), file=archivoS)

print('\nTotal: ' + str(suma), file=archivoS)
archivoS.close()
print('Salida completa')