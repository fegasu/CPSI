from flask import Flask, jsonify,request,redirect, url_for
import json,requests
from flask import render_template
from services.apicnx import Usuario   
from config import configura       
app=Flask(__name__)

@app.route("/niveles/index")
def index():
    return redirect("/niveles/l",code=302)

@app.route("/niveles/<id>",methods=["GET","POST"])
def nivel(id=0):
    return render_template("niveles.html",N=id)

@app.route("/niveles/i",methods=["POST"])
def nivelInserta():
    nom=request.form.get('nom').upper()
    ape=request.form.get('ape').upper()
    u1= Usuario("http://127.0.0.1:5000/usua")
    
    
    datos={
        "NOMBRE":nom,"APELLIDO":ape
    }
    u1.Inserte(datos)
    id=0
    msgitos="Usuario creado satisfactoriamente"
    return render_template("alertas.html",msgito=msgitos)

@app.route("/niveles/u",methods=["POST"])
def nivelactualiza():
    id=request.form.get('id')
    nom=request.form.get('nom')
    ape=request.form.get('ape')
    u1= Usuario("http://127.0.0.1:5000/usua")
    datos={
        "IDUSUARIO":id,"NOMBRE":nom.upper(),"APELLIDO":ape.upper()
    }
    u1.Actualiza(datos)
    id=0
    msgitos="Usuario editado satisfactoriamente"
    return render_template("alertas.html",msgito=msgitos)


@app.route("/niveles/e/<id>",methods=["GET"])
def nivelEdita(id):
    u1= Usuario("http://127.0.0.1:5000/usua")
    cadena=u1.ListarUno(id)
    return render_template("EditarUsuario.html",N=2,cadena=cadena)
@app.route("/niveles/d/<id>",methods=["GET"])
def nivelBorra(id):
    u1= Usuario("http://127.0.0.1:5000/usua")
    cadena=u1.Borra(id)
    msgitos="Usuario borrado satisfactoriamente"
    return render_template("alertas.html",msgito=msgitos)


@app.route("/",methods=["GET"])
def Lista():
    menu=(["Usuarios","Centros","Sedes","Aulas"],["Titulacion","Actividad","Instructor","Coordina"],["Reportes","Regional","Horarios","Acerca de"])
    menu1=(["grupo.png","cforma.png","sedes.png","aulas.png"],["titulacion.png","actividad.png","instructor.png","coordina.png"],["reporte.png","region.png","horario.png","acerca.png"])
    n=len(menu)
    menu=[[
        {"Titulo":"Usuarios","iconos":"grupo.png","enlace":"/niveles/l"},
        {"Titulo":"Centros","iconos":"cforma.png","enlace":"#"},
        {"Titulo":"Sedes","iconos":"sedes.png","enlace":"#"},
        {"Titulo":"Aulas","iconos":"aulas.png","enlace":"#"}],
        [{"Titulo":"Titulacion","iconos":"titulacion.png","enlace": " "},
        {"Titulo":"Actividad","iconos":"actividad.png","enlace":"#"},
        {"Titulo":"Instructor","iconos":"Instructor.png","enlace":"#"},
        {"Titulo":"Coordina","iconos":"coordina.png","enlace":"#"}],
        [{"Titulo":"Reportes","iconos":"reporte.png","enlace":"#"},
        {"Titulo":"Regional","iconos":"region.png","enlace":"#"},
        {"Titulo":"Horarios","iconos":"horario.png","enlace":"#"},
        {"Titulo":"Acerca de","iconos":"acerca.png","enlace":"/niveles/1000"}]
    ]

    return render_template("index.html",menu=menu)

@app.route("/niveles/l",methods=["GET"])
def ListarTodos():
    u1= Usuario("http://127.0.0.1:5000/usua")
    cadena=list(u1.ListarTodos())
    can=len(cadena)
    id=0
    return render_template("niveles.html",N=0,cadena=cadena,can=can)
@app.route("/niveles/1000",methods=["GET"])
def acerca():
    return render_template("acerca.html")
    

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=configura['PUERTOAPP'])    
    