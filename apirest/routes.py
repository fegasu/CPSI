from flask import Flask, jsonify,request,redirect, url_for,session
import json,requests
from flask import render_template
from services.apicnx import Usuario   
from config import configura 

app=Flask(__name__)
app.secret_key="*a6#45$bb"   
#session['bd']=configura['DB']
@app.route("/niveles/i",methods=["POST"])
def nivelInserta():
    nom=request.form.get('nom').upper()
    ape=request.form.get('ape').upper()
    #u1= Usuario()    
    datos={
        "NOMBRE":nom,"APELLIDO":ape
    }
    #u1.Inserte(datos)
    response = requests.post(configura['SERVER_API']+"/usua/i", json=datos)
    id=0
    msgitos="Usuario creado satisfactoriamente"
    return render_template("alertas.html",msgito=msgitos)

@app.route("/niveles/u",methods=["POST"])
def nivelactualiza():
    try:
        id=request.form.get('id')
        nom=request.form.get('nom')
        ape=request.form.get('ape')
        
        datos={
            "IDUSUARIO":id,"NOMBRE":nom.upper(),"APELLIDO":ape.upper()
        }
        response = requests.put(configura['SERVER_API']+"/usua/u", json=datos)
        id=0
        msgitos="Usuario editado satisfactoriamente"
    except Exception as e:
        msgitos="** Error"+response
    return render_template("alertas.html",msgito=msgitos)


@app.route("/niveles/e/<id>",methods=["GET"])
def nivelEdita(id):
    u1= Usuario()
    cadena=u1.ListarUno_a(id)
    return render_template("EditarUsuario.html",cadena=cadena)
    
@app.route("/niveles/d/<id>",methods=["GET"])
def nivelBorra(id):
    
    response = requests.delete(configura['SERVER_API']+"/usua/d/"+id)
    
    msgitos="Usuario borrado satisfactoriamente"
    return render_template("alertas.html",msgito=msgitos)


@app.route("/",methods=["GET"])
@app.route("/ppa",methods=["GET"])
def Lista():
    u1= Usuario()
    cadena=u1.ListarJson("/ppa/menus")
    print(cadena)
    return render_template("index.html",cadena=cadena)
    

@app.route("/niveles/l",methods=["GET"])
def ListarTodos():
    u1= Usuario()
    cadena=list(u1.ListarJson("/ppa/l"))
    can=len(cadena)
    id=0
    return render_template("pusuarios.html",N=0,cadena=cadena)
@app.route("/niveles/1000",methods=["GET"])
def acerca():
    #pyautogui.confirm(text="Mensaje",title="xxxx",buttons=["OK","CANCEL"])
    return render_template("acerca.html")
    

if __name__=='__main__':
    app.run(debug=True,port=8000) 
    