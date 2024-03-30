from flask import Flask, jsonify,request
import json
import sqlite3
con = sqlite3.connect("./usuarios.db")
app=Flask(__name__)

@app.route("/")
def inicio():
    return "Hola"
@app.route("/usua")
def ListaUsuario():
    con = sqlite3.connect("usuarios.db")
    cur = con.cursor()
    sql="select * from USUA"
    res=cur.execute(sql)
    todo=res.fetchall()
    return json.dumps(todo)
@app.route("/usua/<id>")
def ListaUnUsuario(id):
    con = sqlite3.connect("usuarios.db")
    cur = con.cursor()
    sql="select * from USUA where IDUSUA="+str(id)
    res=cur.execute(sql)
    todo=res.fetchall()
    return json.dumps(todo)

@app.route("/usua/i",methods = ['POST'])
def CrearUsuario(): 
    datos=request.get_json()  
    con = sqlite3.connect("usuarios.db")
    ape=datos['APELLIDO']
    nom=datos['NOMBRE']
    sql="insert into USUA(NOMBRE,APELLIDO) values('"+nom+"','"+ape+"')"

    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    
    return "nada de nada"
@app.route("/usua/u",methods = ['PUT'])
def EditaUsuario(): 
    con = sqlite3.connect("usuarios.db")
    datos=request.get_json()
    id=datos['IDUSUARIO']
    ape=datos['APELLIDO']
    nom=datos['NOMBRE']
    sql="update USUA set NOMBRE='"+nom+"',APELLIDO='"+ape+"' where IDUSUA="+str(id)
    print(sql)
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    return "OK"
@app.route("/usua/d/<id>",methods = ['DELETE'])
def BorrarUsuario(id): 
    con = sqlite3.connect("usuarios.db")
    sql="delete from USUA where IDUSUA="+str(id)
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    return "OK"
    
if __name__=='__main__':
    app.run(debug=True)