from flask import Flask, jsonify,request
import json
import sqlite3
bd="sinsonte.db"



def ConsultarJson(sql):
        con = sqlite3.connect("api\sinsonte.db")
        todo=[]     
        cur = con.cursor()  
        res=cur.execute(sql)
        nombres_columnas = [descripcion[0] for descripcion in cur.description]
        print("*******>",nombres_columnas)
        primer_resultado = res.fetchall()
    
        for i,valor in enumerate(primer_resultado):
            aux1=valor
            aux2= nombres_columnas
            aux3=dict(zip(aux2,aux1))   
            todo.append(aux3)
        con.close() 
        return list(todo)  


    
app=Flask(__name__)
@app.route("/")
def Inicio():
    return "SINSONTE"
@app.route("/t")
def ListaUsuario():
    sql="select * from unidad"
    todo=ConsultarJson(sql)    
    return json.dumps(todo)

@app.route("/t/<id>")
def ListaUnUsuario(id):
    sql="select * from UNIDAD where IDUNIDAD="+str(id)
    todo=ConsultarJson(sql)
    return json.dumps(todo)

if __name__=='__main__':
    app.run(debug=True,port=8000,host='0.0.0.0')
