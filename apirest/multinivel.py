from flask import Flask, jsonify,request
import json,requests
from flask import render_template
from services.apicnx import Usuario       

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return render_template("niveles.html",N="2")
@app.route("/niveles/<id>",methods=["GET","POST"])
def nivel(id=0):
    return render_template("niveles.html",N=id)

@app.route("/niveles/i",methods=["POST"])
def nivelInserta():
    nom=request.form.get('nom')
    ape=request.form.get('ape')
    u1= Usuario("http://127.0.0.1:5000/usua")
    datos={
        "NOMBRE":nom,"APELLIDO":ape
    }
    u1.Inserte(datos)
    return "Ok1"

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)