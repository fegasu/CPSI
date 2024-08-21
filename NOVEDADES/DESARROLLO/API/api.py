from flask import Flask,render_template,request,redirect
import requests
from flask_cors import CORS
import sqlite3

def create_app():
    app=Flask(__name__)
    CORS(app)
    return app

app = create_app() # CREATE THE FLASK APP

@app.route("/ln/<tipo>")
def listar(tipo):
    return "Listar"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)