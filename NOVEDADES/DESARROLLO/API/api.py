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

@app.route("/ln")
def listar():    
    try:
        con = sqlite3.connect("nov.db")
    except:
        return("Ocurrio un error")
    
    cur = con.cursor()
    
    sql="select * from novedades n, ambiente a  where estado=0 and a.idambiente=n.idambiente"
    res=cur.execute(sql)
    todo=res.fetchall()
    con.close() 
    return json.dumps(todo)
    

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)