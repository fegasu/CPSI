'''
nombre #atributo público
_nombre #atributo protegido
__nombre #atributo privado
'''
class Alumno:
  def __init__(self, nombre, nota):
    self.__nombre = nombre
    self.__nota = nota
    print ("Estoy dentro del constructor")

  def mostrar_info(self, maximo=5):
    print ("nombre", self.__nombre, "nota:", self.__nota, "entre ", maximo)
    print ("Objeto actual ", self)
########################################
a1 = Alumno ("Juan", 3)

a1.mostrar_info()


a2 = Alumno ("Margarita", 3)
a2.mostrar_info(4)
print(a2)
print (a2)
