from flask import Flask, jsonify,request
from flask import render_template
app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return render_template("niveles.html",N="2")
@app.route("/niveles/<id>",methods=["GET","POST"])
def nivel(id=0):
    return render_template("niveles.html",N=id)

@app.route("/niveles/i",methods=["POST"])
def nivelInserta():
    nom=request.form.get('nom')
    ape=request.form.get('ape')
    datos={
        "NOMBRE":nom,"APELLIDO":ape
    }
    api_url="http://127.0.0.1:5000/usua/i"
    response = requests.post(api_url, json=datos)
    return nom

if __name__=='__main__':
    app.run(debug=True,port=8000)