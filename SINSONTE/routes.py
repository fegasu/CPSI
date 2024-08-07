
from flask import Flask,render_template,request
import requests
from flask_cors import CORS
from api.apicnx import *
from api.config import configura
def create_app():
    app=Flask(__name__)
    CORS(app)
    return app

app = create_app() # CREATE THE FLASK APP
@app.route("/")
def inicio():
    return render_template("otro.html")
@app.route("/logo")
def inilogocio():
    return render_template("banner.html")
@app.route("/menu")
def menup():
    return render_template("menu.html")
@app.route("/unidad")
def Unidad():
    u1=Usuario()
    cadena=u1.ListarJson("/t")
    print(cadena)
    if cadena==None:
        cadena=[]
        v=0
    else:
        v=1
    N=0
    if cadena==None:
        return render_template("unidad.html",N=N,url=configura['PUERTOREST'],V=v)
    else:
        return render_template("unidad.html",N=N,url=configura['PUERTOREST'],cadena=list(cadena),V=v)
        
@app.route("/u/d/<id>")
def BorraUnidad3(id):
    print("*****>",id)
    N=3
    return render_template("unidad.html",N=N,url=configura['PUERTOREST'],ID=id)
@app.route("/u/d31",methods=["POST","DELETE"])
def BorraUnidad31():
    N=0
    u1=Usuario()
    id=request.form['idu']
    u1.BorraAPI(id,'/t/d/')
    
    cadena=u1.ListarJson("/t")
    if cadena==None:
        cadena=[]
        v=0
    else:
        v=1
    return render_template("unidad.html",N=N,url=configura['PUERTOREST'],cadena=cadena,V=v,msg="Borrado")
@app.route("/u/i")
def NuevaUnidad():
    N=1
    
    return render_template("unidad.html",N=N)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)