
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
    N=0
    return render_template("unidad.html",N=N,url=configura['PUERTOREST'],cadena=cadena)
@app.route("/u/d/<id>")
def BorraUnidad3(id):
    N=3
    return render_template("unidad.html",N=N,url=configura['PUERTOREST'])
@app.route("/u/d31/<id>")
def BorraUnidad31(id):
    N=31
    u1=Usuario()
    u1.BorraAPI(id,'/t/d/')
    return render_template("unidad.html",N=N,url=configura['PUERTOREST'])

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)