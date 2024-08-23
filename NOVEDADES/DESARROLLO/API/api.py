from flask import Flask,render_template,request,redirect
import requests
from flask_cors import CORS
import sqlite3
import json
from  services.adaptador import *
def create_app():
    app=Flask(__name__)
    CORS(app)
    return app

app = create_app() # CREATE THE FLASK APP
app.bd="nov.db"

@app.route("/ln")
def listar():    
    try:
        con = sqlite3.connect("nov.db")
    except:
        return("Ocurrio un error")
    
    cur = con.cursor()
    
    sql="select * from vambiente"
    u1=Usuario(app.bd)
    todo=u1.ConsultarJson(sql)
    return(todo)
     
    # return json.dumps(todo)
@app.route("/ln/<ambi>")
def listarOne(ambi):    
    
    sql="select * from vambiente where idambiente="+ambi
    u1=Usuario(app.bd)
    todo=u1.ConsultarJson(sql)
    return(todo)
@app.route("/ln/<estado>/<amb>")
def listarNovXamb(estado,amb):    
    
    estado=estado.upper()
    if estado=="A":
        estado="ABIERTA"
    elif estado=="P":
        estado="PROCESO"
    elif estado=="C":
        estado="CERRADA"
    
    if amb !="0":
        sql="select * from vambiente where estado='"+estado+"' and idambiente="+amb
    else:
        sql="select * from vambiente where estado='"+estado+"'"
    print(sql)    
    u1=Usuario(app.bd)
    todo=u1.ConsultarJson(sql)
    return(todo)
@app.route("/e/<amb>")
def equiparesumen(amb):    
    if amb !="0":
        sql="select * from EQUIRESUMEN where  idambiente="+amb
    else:
       sql="select * from EQUIRESUMEN" 
    
    u1=Usuario(app.bd)
    todo=u1.ConsultarJson(sql)
    return(todo)
@app.route("/e/a/<amb>")
def equipamiento(amb):    
    if amb !="0":
        sql="select * from VEQUIPAMIENTO where  idambiente="+amb
    else:
       sql="select * from VEQUIPAMIENTO" 
    
    u1=Usuario(app.bd)
    todo=u1.ConsultarJson(sql)
    return(todo)
@app.route("/n/<nove>")
def actualizanov(nove):    
    sql="select * from VNOVEDADUNO where  idnovedades="+nove    
    u1=Usuario(app.bd)
    todo=u1.ConsultarJson(sql)
    return(todo)
 
  
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)