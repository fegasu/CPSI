import json,requests
from services.apicnx import Usuario       

u1= Usuario("http://127.0.0.1:5000/usua")
#print(u1.ListarTodos())
#print(u1.ListarUno(16))



emp={
    "NOMBRE":"Soila","APELLIDO":"Vaca del corrar"
}
u1.Inserte(emp)
#u1.Borra(37)
'''

emp={
    "IDUSUARIO":36,"NOMBRE":"Soila","APELLIDO":"Vaca del Corral"
}
u1.Actualiza(emp)
'''
print(u1.ListarTodos())

