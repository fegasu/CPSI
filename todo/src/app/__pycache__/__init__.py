from flask import Flask
from flask_cors import CORS
from region.routes import region
def create_app():
    app=Flask(__name__)
    CORS(app)
    app.register_blueprint(region)
    return app

