# imports
from flask import Blueprint, jsonify, request, abort
from flask_pymongo import ObjectId, MongoClient
from jwt import encode
from datetime import datetime, timedelta # for the user registration time
import hashlib # to make a hash of the user's password (strongly recommended)

user = Blueprint('user', __name__, url_prefix='/user')

# If user exist
def existing_user(user):
    return 'Existe'

@user.route('/l', methods=['GET'])
def new_user():
    return "Hola"
