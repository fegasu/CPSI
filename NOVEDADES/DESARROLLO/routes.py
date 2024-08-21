from flask import Flask,render_template,request,redirect
import requests
from flask_cors import CORS

def create_app():
    app=Flask(__name__)
    CORS(app)
    return app

app = create_app() # CREATE THE FLASK APP
@app.route("/")
def inicio():
    return render_template("index.html")
@app.route("/menu")
def menu():
    return render_template("menu.html")
@app.route("/banner")
def banner():
    return render_template("banner.html")
@app.route("/centro")
def centro():
    return render_template("centro.html")
@app.route("/footer")
def footer():
    return render_template("footer.html")


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)