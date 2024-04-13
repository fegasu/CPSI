class Cuenta:
    def __init__(self,numero,tipo,saldo):
        self.__numero=numero
        self.__tipo=tipo
        self.__saldo=saldo
    def getNumero(self):
      return self.__numero
    def getTipo(self):
        return self.__tipo
    def getSaldo(self):
        return self.__saldo
      
class Cliente: 
  def __init__(self,ced,nom,numerocta,tipo,saldo):
    self.__cedula=ced
    self.__nombre=nom
    self.cuenta=Cuenta(numerocta,tipo,saldo)
  def getCed(self):
    return self.__cedula
  def getNom(self):
    return self.__nombre
  def getNum(self):
    return self.cuenta.getNumero()
  def getTipo(self):
    return self.cuenta.getTipo()
  def getSaldo(self):
    return self.cuenta.getSaldo()

class Banco:
  numclientes=0
  def __init__(self,nombre):
    self.__nombre=nombre
    self.cliente=[]
    self.numclientes=self.numclientes+1

  def Adicionar_cliente(self,cliente:Cliente):
    self.cliente.append(cliente)
  def getNom(self):
      return self.__nombre  
  def obtener_numero(self):
    return len(self.cliente)

  def obtener_clientes(self):
    for x in self.cliente:
      print(self.getNom(),x.getCed(),x.getNom(),x.getNum(),x.getTipo(),x.getSaldo())
  def ver_info_clientes(self):
    pass
  def total_saldos_ahorro(self):
        self.saldoAhorros=0
        for x in self.cliente:
            if x.getTipo()==1:
                self.saldoAhorros=self.saldoAhorros+x.getSaldo()
        return self.saldoAhorros
  def total_saldos_corriente(self):
        pass
  def total_saldos_corriente(self):
        self.saldoAhorros=0
        for x in self.cliente:
            if x.getTipo()==2:
                self.saldoAhorros=self.saldoAhorros+x.getSaldo()
        return self.saldoAhorros
c1=Cliente(12345,'Uldarico',1089,1,1000)
b1=Banco("Citibanck")
b1.Adicionar_cliente(c1)
c2=Cliente(67890,'Sandra',246,2,5000)
b1.Adicionar_cliente(c2)
c3=Cliente(2233,'Rosa Melano',333,2,2000)
b1.Adicionar_cliente(c3)
c4=Cliente(4455,'Simon Tolomeo',444,1,2500)
b1.Adicionar_cliente(c4)
print("numero de clientes:",b1.obtener_numero())
b1.obtener_clientes()
print("Saldo de ahorros:",b1.total_saldos_ahorro())
print("Saldo de Corriente:",b1.total_saldos_corriente())