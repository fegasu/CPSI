# imports
from flask import Blueprint, jsonify, request, abort,redirect, url_for
from flask import render_template
from jwt import encode
from datetime import datetime, timedelta # for the user registration time
import hashlib # to make a hash of the user's password (strongly recommended)

region = Blueprint('region', __name__, url_prefix='/r',
                        template_folder='templates')

# If user exist
def existing_regin(region):
    return 'Existe'

@region.route('/l', methods=['GET'])
def new_region():
    return render_template("uno.html",N=id)

@region.route('/')
def show():
    return "Otro"