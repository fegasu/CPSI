from abc import ABC, abstractmethod
class ReinoAnimal(ABC):
  def comen(self,tipo):
    pass
  def nacen(self,tipo):
    pass
class CNACEN(ReinoAnimal):
  def comen(self,tipo):
    pass
  def nacen(self,tipo):
    if tipo==1:
          print("OVIPAROS Nace de huevos")
    if tipo==2:
          print("VIVIPAROS Se forman dentro de la madre")
class CALIMENTAN(ReinoAnimal):
      def nacen(self,tipo):
            pass
      def comen(self,tipo):
        if tipo==1:
              print("HERVIVOROS comen hiervas")
        if tipo==2:
              print("CARNIVOROS comen carne")
        if tipo==3:
              print("OMNIVOROS comen hierva y carne ")
class Oviparos(CNACEN):
      def __init__(self):
            self.nacen(1)
class Viviparos(CNACEN):
      def __init__(self):
            self.nacen(2)
class Hervivoros(CALIMENTAN):
      def __init__(self):
            self.comen(1)
class Carnivoros(CALIMENTAN):
      def __init__(self):
            self.comen(2)
class Ovnivoros (CALIMENTAN):
      def __init__(self):
            self.comen(3)
viviparo =  Viviparos()
oviparo =  Oviparos()
hervivoros= Hervivoros()
carnivoros= Carnivoros()          
ovnivoros= Ovnivoros()
    