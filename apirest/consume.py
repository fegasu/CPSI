import json,requests
from services.apicnx import Usuario       

u1= Usuario("http://127.0.0.1:5000/usua")
print(u1.ListarTodos())
#print(u1.ListarUno(5))



emp={
    "NOMBRE":"Simon","APELLIDO":"TAPICHA RICO"
}
#u1.Inserte(emp)
#u1.Borra(8)

emp={
    "IDUSUARIO":4,"NOMBRE":"CARLOS","APELLIDO":"VILLAGRAN"
}
#u1.Actualiza(emp)

