import json,requests
import sqlite3
class cnxsqlite:
    def Consultar(self,bd,sql):
        con = sqlite3.connect(bd)
        cur = con.cursor()
        res=cur.execute(sql)
        todo=res.fetchall()
        con.close() 
        return json.dumps(todo)   
    def Ejecutar(self,bd,sql):
        con = sqlite3.connect(bd)
        cur = con.cursor()
        res=cur.execute(sql)
        con.commit()
        con.close()  

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
        self.res=requests.get(self.url)
        data1=json.loads(self.res.content)
        return data1
    def ListarUno(self,cual=0):    
        self.res=requests.get(self.url+"/"+str(cual))
        data1=json.loads(self.res.content)
        if data1!=[]:
            return(data1)
        else:
            return False  
    def Inserte(self,data):
            response = requests.post(self.url+"/i", json=data)
    def Borra(self,cual):
        response = requests.delete(self.url+"/d/"+str(cual))
    def Actualiza(self,data):
        response = requests.put(self.url+"/u", json=data)
