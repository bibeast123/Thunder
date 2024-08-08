""" Entry Point to Flask App"""
import os
from flask import Flask, jsonify, request
from sqlalchemy.dialects.sqlite import JSON
from flask_cors import CORS
from .configs import *
from .src.helpers.trascriber import *
from .src.ml.summarize import *
from .src.services import service 
from .src.models.models import db, User
from .src.helpers.logger import logData

app = Flask(__name__)

# Runtime Configs
logData("========= Starting App =========")
CORS(app, resources = {r"/*":{"origins":"*"}})
DB_PATH = 'sqlite:///' + os.path.dirname(os.path.realpath(__file__)) + '/db/users.db'
app.config['SQLALCHEMY_DATABASE_URI'] = DB_PATH
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Database Setup
db.init_app(app)
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    """Show users in database"""
    return BASE_ENDPOINT_STRING

# Gets all users
@app.route('/users')
def get_users():
    return jsonify(service.get_users(User))

# Gets a user
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return jsonify(service.get_user(User, user_id))

# Deletes all users
@app.route('/users', methods=['DELETE'])
def delete_users():
    return jsonify(service.delete_users(db, User))

# Deletes a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return jsonify(service.delete_user(db, User, user_id))

# Updates a user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    return jsonify(service.update_user(db, User, user_id, request))

# Get transcription of audio
@app.route("/ml/transcribe/<int:user_id>", methods=['GET'])
def get_transcription(user_id):
    return jsonify(service.get_transcription(User, user_id))

# Get summary of transcription
@app.route("/ml/summary/<int:user_id>", methods=['GET'])
def get_summary(user_id):
    return jsonify(service.get_summary(User, user_id))

@app.route('/ml/solutions/<int:user_id>', methods=['GET'])
def get_solutions(user_id):
    return jsonify(service.get_solutions(User, user_id))

@app.route('/ml/categorize/<int:user_id>', methods=['GET'])
def categorize(user_id):
    return jsonify(service.categorize(User, user_id))

if __name__ == '__main__':
    app.run(debug=True)
