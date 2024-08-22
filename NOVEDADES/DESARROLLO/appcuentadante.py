from flask import Flask,render_template,request,redirect
import requests
from flask_cors import CORS
import json

def create_app():
    app=Flask(__name__)
    CORS(app)
    return app
app = create_app() # CREATE THE FLASK APP
app.ruta="http://127.0.0.1:8000"

class Usuario:
    
    res=None
    data=None
    def __init__(self):
        self.url=app.ruta
        print("---->",app.ruta)


    def ListarTodos(self,clave="/ln"):
        
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


@app.route("/")
def inicio():
    return render_template("index.html")
@app.route("/menu")
def menu():
    return render_template("menu.html")
@app.route("/banner")
def banner():
    return render_template("banner.html")
@app.route("/centro")
def centro():
    return render_template("centro.html")
@app.route("/footer")
def footer():
    return render_template("footer.html")
@app.route("/novedada")
def novedada():
    u1=Usuario()
    cadena=u1.ListarJson("/ln/a/1")
    llenos=1
    msg="NOVEDADES ABIERTAS"
    if cadena==False:
        return render_template("novedades.html",cadena=cadena,hay=0,msg=msg)
    return render_template("novedades.html",cadena=cadena,hay=1,msg=msg)
@app.route("/novedadp")
def novedadp():
    u1=Usuario()
    cadena=u1.ListarJson("/ln/p/1")
    msg="NOVEDADES EN PROCESO"
    
    if cadena==False:
        return render_template("novedades.html",cadena=cadena,hay=0,msg=msg)
    return render_template("novedades.html",cadena=cadena,hay=1,msg=msg)

@app.route("/novedadc")
def novedadc():
    u1=Usuario()
    cadena=u1.ListarJson("/ln/c/1")
    llenos=1
    msg="NOVEDADES CERRADAS"
    
    if cadena==False:
        return render_template("novedades.html",cadena=cadena,hay=0,msg=msg)
    return render_template("novedades.html",cadena=cadena,hay=1,msg=msg)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)