
from flask import Flask,render_template,request
from flask_cors import CORS
def create_app():
    app=Flask(__name__)
    CORS(app)
    return app

app = create_app() # CREATE THE FLASK APP
@app.route("/")
def inicio():
    return render_template("otro.html")
@app.route("/logo")
def inilogocio():
    return render_template("banner.html")
@app.route("/menu")
def menup():
    return render_template("menu.html")
@app.route("/unidad")
def x():
    return render_template("unidad.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)