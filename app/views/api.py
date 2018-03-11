# Copyright 2014 SolidBuilds.com. All rights reserved
#
# Authors: Ling Thio <ling.thio@gmail.com>


from flask import Blueprint, jsonify, current_app as app, request
from app.models.user_models import User

# When using a Flask app factory we must use a blueprint to avoid needing 'app' for '@app.route'
api_blueprint = Blueprint('api', __name__, template_folder='templates')

# The Home page is accessible to anyone
@api_blueprint.route('/')
def home():
    d = {"status": 401, "message": "No resources here"}
    return jsonify(d)

@api_blueprint.route('/user/<uuid>')
def user(uuid):
    d = {
            "status": 200,
            "display_name": "David Tyoember"
        }
    return jsonify(d)


@api_blueprint.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    user = User.query.filter_by(email=email).first_or_404()
    verified = app.user_manager.verify_password(password, user)
    status = 403
    if verified:
        status = 200
    d = {
            "status": status
    }
    return jsonify(d)
