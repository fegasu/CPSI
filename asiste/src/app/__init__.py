# imports
from flask import Flask
from flask_cors import CORS

# Here we're gonna import the blueprints
from ppal.routes import ppal



# function than create a flask app with CORS
def create_app():
    app = Flask(__name__)
    CORS(app)

    # Here we're gonna register the blueprints
    app.register_blueprint(ppal)
    return app