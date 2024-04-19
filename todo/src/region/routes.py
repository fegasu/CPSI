# imports
from flask import Blueprint, jsonify, request, abort
from flask_pymongo import ObjectId, MongoClient
from jwt import encode
from datetime import datetime, timedelta # for the user registration time
import hashlib # to make a hash of the user's password (strongly recommended)

region = Blueprint('region', __name__, url_prefix='/r')

# If user exist
def existing_regin(region):
    return 'Existe'

@region.route('/l', methods=['GET'])
def new_region():
    return "Hola"
