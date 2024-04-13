class Motor:
  def __init_(self,tipo):
    self.tipo=tipo
  def arrancar(self):
    print("Motor arrancado")
  
class Coche:
  def __init__(self,modelo,tipoMotor):
    self.__modelo=modelo
    self.__tipoMotor=tipoMotor
  def getModelo(self):
        return self.__modelo
  def conducir(self):
    print("Conduciendo el coche modelo: "+self.getModelo())
    
miCoche=Coche("Sedan","Gasolina")
miCoche.conducir()
