from flask import Flask, jsonify,request
from flask import render_template
app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return render_template("niveles.html",N="2")
@app.route("/niveles/<id>",methods=["GET","POST"])
def nivel(id=0):
    return render_template("niveles.html",N=id)
if __name__=='__main__':
    app.run(debug=True,port=8000)