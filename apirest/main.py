from flask import Flask, jsonify,request
import json
#from services.apicnx import cnxsqlite
from api.cnxSqlite import cnxsqlite  
from config import configura 
import sqlite3
bd=configura['DB']
#session['bd']=configura['DB']
rutapi=configura['SERVER_NAME']+":"+str(configura['SERVER_NAME'])
print("* Base de datos:",bd)

app=Flask(__name__)
@app.route("/")
def inicio():
    return "CENTRO DE PRODUCCION DE SOLUCIONES INTELIGENTES - CPSI -"

@app.route("/ppa")
@app.route("/ppa/l")
def ListaUsuario():
    sql="select * from USUA" 
    con=cnxsqlite()   
    todo=con.ConsultarJson(sql)
    return json.dumps(todo)
@app.route("/ppa/<id>")
@app.route("/usua/<id>")
def ListaUnUsuario(id):
    sql="select * from USUA where IDUSUA="+str(id)
    con=cnxsqlite()
    todo=con.ConsultarJson(sql)
    return json.dumps(todo)

@app.route("/usua/i",methods = ['POST'])
def CrearUsuario(): 
    datos=request.get_json()  
    ape=datos['APELLIDO']
    nom=datos['NOMBRE']
    sql="insert into USUA(NOMBRE,APELLIDO) values('"+nom+"','"+ape+"')"
    print(sql)
    con=cnxsqlite()   
    todo=con.Ejecutar(sql)
    return "OK"
@app.route("/usua/u",methods = ['PUT'])
def EditaUsuario(): 
    datos=request.get_json()
    id=datos['IDUSUARIO']
    ape=datos['APELLIDO']
    nom=datos['NOMBRE']
    sql="update USUA set NOMBRE='"+nom+"',APELLIDO='"+ape+"' where IDUSUA="+str(id)
    print(sql)
    con=cnxsqlite()
    todo=con.Ejecutar(sql)
    return "Usuario editado satisfactoriamente"
@app.route("/usua/d/<int:id>",methods = ['DELETE'])
def BorrarUsuario(id): 
    #datos=request.get_json()
    try:
        sql="delete from USUA where IDUSUA=?"
        con = sqlite3.connect(bd)
        cur = con.cursor()
        cur.execute(sql,(id,))
        con.commit()
        con.close()
    except Exception as e:
        return str(e)+" "+sql
        
@app.route("/ppa/menus",methods=['GET'])
def VerMenu():
    sql="select * from MODULOS"
    con=cnxsqlite()
    todo=con.ConsultarJson(sql)
    return jsonify(todo)
@app.route("/ppa/centros",methods=['GET'])
def ListaCentros():
    sql="select * from CENTROS" 
    con=cnxsqlite()   
    todo=con.ConsultarJson(sql)
    return json.dumps(todo)
@app.route("/ppa/centros/<int:id>",methods=['GET'])
def ListaCentrosUno(id):
    sql="select * from CENTROS WHERE IDCENTRO=" + str(id)
    con=cnxsqlite()   
    todo=con.ConsultarJson(sql)
    return json.dumps(todo)
@app.route("/ppa/centros/u",methods = ['PUT'])
def EditaCentros(): 
    datos=request.get_json()
    id=datos['IDUSUARIO']
    nom=datos['NOMBRE']
    sql="update CENTROS set NOMBRE='"+nom+"' where IDCENTRO="+str(id)
    print(sql)
    con=cnxsqlite()
    todo=con.Ejecutar(sql)
    return "Centro editado satisfactoriamente"

@app.route("/centros/d/<int:id>",methods = ['DELETE'])
def BorrarCentros(id): 
    #datos=request.get_json()
    try:
        sql="delete from CENTROS where IDCENTRO=?"
        con = sqlite3.connect(bd)
        cur = con.cursor()
        cur.execute(sql,(id,))
        con.commit()
        con.close()
    except Exception as e:
        return str(e)+" "+sql
@app.route("/centros/i",methods = ['POST'])
def CrearCentro(): 
    datos=request.get_json()  
    nom=datos['NOMBRE']
    sql="insert into CENTROS(NOMBRE) values('"+nom+"')"
    print(sql)
    con=cnxsqlite()   
    todo=con.Ejecutar(sql)
    return "OK"
@app.route("/ppa/sedes")
def ListaSedes():
    sql="select * from SEDES" 
    con=cnxsqlite()   
    todo=con.ConsultarJson(sql)
    return json.dumps(todo)
    
if __name__=='__main__':
    app.run(debug=True,port=configura['PUERTOREST'],host='0.0.0.0')