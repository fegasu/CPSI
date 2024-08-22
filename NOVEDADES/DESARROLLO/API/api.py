from flask import Flask,render_template,request,redirect
import requests
from flask_cors import CORS
import sqlite3
import json

def create_app():
    app=Flask(__name__)
    CORS(app)
    return app

app = create_app() # CREATE THE FLASK APP
app.bd="nov.db"
def ConsultarJson(sql):
        con = sqlite3.connect(app.bd)
        todo=[]
        cur = con.cursor()
        res=cur.execute(sql)
        nombres_columnas = [descripcion[0] for descripcion in cur.description]
        print(nombres_columnas)
        primer_resultado = res.fetchall()
    
        for i,valor in enumerate(primer_resultado):
            aux1=valor
            aux2= nombres_columnas
            aux3=dict(zip(aux2,aux1))   
            todo.append(aux3)
        con.close() 
        return list(todo)  

@app.route("/ln")
def listar():    
    try:
        con = sqlite3.connect("nov.db")
    except:
        return("Ocurrio un error")
    
    cur = con.cursor()
    
    sql="select * from vambiente"
    todo=ConsultarJson(sql)
    return(todo)
     
    # return json.dumps(todo)
@app.route("/ln/<ambi>")
def listarOne(ambi):    
    try:
        con = sqlite3.connect("nov.db")
    except:
        return("Ocurrio un error")
    
    cur = con.cursor()
    
    sql="select * from vambiente where idambiente="+ambi
    todo=ConsultarJson(sql)
    return(todo)
@app.route("/ln/<estado>/<amb>")
def listarNovXamb(estado,amb):    
    try:
        con = sqlite3.connect("nov.db")
    except:
        return("Ocurrio un error")
    estado=estado.upper()
    if estado=="A":
        estado="ABIERTA"
    elif estado=="P":
        estado="PROCESO"
    elif estado=="C":
        estado="CERRADA"
    cur = con.cursor()
    if amb !="0":
        sql="select * from vambiente where estado='"+estado+"' and idambiente="+amb
    else:
        sql="select * from vambiente where estado='"+estado+"'"
    print(sql)    
    todo=ConsultarJson(sql)
    return(todo)
@app.route("/e/<amb>")
def equiparesumen(amb):    
    try:
        con = sqlite3.connect("nov.db")
    except:
        return("Ocurrio un error")
    
    cur = con.cursor()
    if amb !="0":
        sql="select * from EQUIRESUMEN where  idambiente="+amb
    else:
       sql="select * from EQUIRESUMEN" 
    
        
    res=cur.execute(sql)
    todo=res.fetchall()
    con.close() 
    return json.dumps(todo)
 
  
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)