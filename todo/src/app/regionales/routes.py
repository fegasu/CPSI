from flask import request,jsonify,Blueprint
regionales=Blueprint("regionales",__name__,import_name="/R")
@regionales.route('/new',methods=['GET'])
def inicio():
    return "hola"