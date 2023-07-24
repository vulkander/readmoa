
import uuid
from datetime import date, datetime



from flask import Flask, jsonify, request, url_for
from flask.json import JSONEncoder
from flask_cors import CORS
from werkzeug.routing import BaseConverter
from .config import config_by_name


# instantiate the app
app = Flask(__name__)
app.config.from_object(config_by_name['dev'])

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


#firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('./read-moa-ce66e5b11aa2.json')
firebase_admin.initialize_app(cred)

db = firestore.client()



#controller
from app import controller

