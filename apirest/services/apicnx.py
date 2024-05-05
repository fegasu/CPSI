import json,requests
from config import configura 
class Usuario:

    res=None
    data=None
    def __init__(self):
        
        self.bd=configura['DB']
        self.url=configura['SERVER_NAME']+":"+str(configura['PUERTOREST'])

    def ListarTodos(self,clave="/to"):
        self.res=requests.get(self.url+clave)
        data1=json.loads(self.res.content)
        return data1
    def ListarUno_a(self,cual):    
        self.res=requests.get(self.url+"/ppa/"+str(cual))
        data1=json.loads(self.res.content)
        if data1!=[]:
            return(data1)
        else:
            return False  
    def ListarJson(self,clave):    
        self.res=requests.get(self.url+clave)
        data1=json.loads(self.res.content)
        if data1!=[]:
            return(data1)
        else:
            return False  
    def Inserte(self,data,clave="/i"):
        print(self.url+clave)
        response = requests.post(self.url+clave, json=data)
    def Borra(self,cual,clave):
        response = requests.delete(self.url+clave+str(cual))
    def Actualiza(self,data,clave="/u"):
        response = requests.put(self.url+clave, json=data)
