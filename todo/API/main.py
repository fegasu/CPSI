from flask import Flask, jsonify,request

import json

#from services.apicnx import cnxsqlite
from database.cnxSqlite import cnxsqlite  
from config import configura 
app=Flask(__name__)
@app.route("/")
def inicio():
    return "Hola"
@app.route("/usua/cc")

@app.route("/usua/to")
def ListaUsuario():
    sql="select * from USUA" 
    con=cnxsqlite()   
    todo=con.Consultar("./usuarios.db",sql)
    return json.dumps(todo)
if __name__=='__main__':
    app.run(debug=True,port=configura['PUERTOREST'],host='0.0.0.0')