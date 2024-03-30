import json,requests
class cnx:
    def ListarTodos(self):
        pass
    def Inserte(self,api_url,data):
        pass
    def ListarUno(self,cual=0):
        pass
    def Borra(self,cual):
        pass
    def Actualiza(self,data):
        pass    
    
class Usuario(cnx):
    url=None
    res=None
    data=None
    def __init__(self,murl):
        self.res=requests.get(murl)
        self.data=json.loads(self.res.content)
        self.url=murl
        response = requests.get(murl)
        #print(self.data)
    def ListarTodos(self):
        return self.data
    def ListarUno(self,cual=0):    
        self.res=requests.get(self.url+"/"+str(cual))
        data1=json.loads(self.res.content)
        if data1!=[]:
            return(data1)
        else:
            return False  

    def Inserte(self,api_url,data):
        response = requests.post(api_url, json=data)
    def Borra(self,cual):
        response = requests.delete(self.url+"/d/"+str(cual))
    def Actualiza(self,data):
        response = requests.put(self.url+"/u", json=data)
       

u1= Usuario("http://127.0.0.1:5000/usua")
print(u1.ListarTodos())
#print(u1.ListarUno(5))



emp={
    "NOMBRE":"Simon","APELLIDO":"TAPICHA"
}
#u1.Inserte("http://127.0.0.1:5000/usua/i",emp)
u1.Borra(8)

emp={
    "IDUSUARIO":4,"NOMBRE":"CARLOS","APELLIDO":"VILLAGRAN"
}
#u1.Actualiza(emp)

