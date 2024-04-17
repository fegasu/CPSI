from flask import Flask
from flask import CORS
def create_app():
    app=Flask(__name__)
    CORS(app)
    
    return app