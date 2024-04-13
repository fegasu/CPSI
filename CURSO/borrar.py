import random
class Persona:
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad

  @staticmethod    #este es un método estático
  def mensaje_hoy():
    mensajes =["La vida es bella", "Mejor tarde que nunca", "Dios te bendiga", "Vive para servir"]
    print (random.choice(mensajes))

  def mostrar_info(self):
    print (f"{self.nombre} tiene {self.edad} años")
####################################################################################################
Persona.mensaje_hoy()
p1 = Persona ("Pablo", 38)
p1.mostrar_info()
Persona.mensaje_hoy()