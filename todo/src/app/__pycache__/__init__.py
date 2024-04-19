from flask import Flask
from flask_cors import CORS
from regionales.routes import regionales
def create_app():
    app=Flask(__name__)
    CORS(app)
    app.register_blueprint(regional)
    return app

