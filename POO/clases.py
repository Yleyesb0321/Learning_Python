#Creando clases, se utiliza la palabra 'class' seguido del nombre de la clase
class Invitado:
  'Clase común para todos los inivtados'
  
  #Se crea el metodo constructor con 'def _init_'
  def __init__(self, nombre, tiquetes):
    self.nombre = nombre
    self.tiquetes = tiquetes
  
  #Se crean los metodos para Mostrar invitados y Agregar tiquetes
  def mostrarInvitados(self):
    print('Nombre : {}, Tiquetes : {}'.format(self.nombre, self.tiquetes))
    
  def agregarTiquetes(self):
    self.tiquetes += 1
    print('{} el número de tiquetes ahora es {}'.format(self.nombre, self.tiquetes))
    
#Probamos la clase creando las instancias
invitado1 = Invitado('Miguel K', 5)
invitado2 = Invitado('Catalina P', 3)

#Mostramos los metodos dentro de las instancias
invitado1.mostrarInvitados()
invitado2.mostrarInvitados()
invitado2.agregarTiquetes()
invitado2.agregarTiquetes()