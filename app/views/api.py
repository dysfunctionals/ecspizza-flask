# Copyright 2014 SolidBuilds.com. All rights reserved
#
# Authors: Ling Thio <ling.thio@gmail.com>


from flask import Blueprint, jsonify

# When using a Flask app factory we must use a blueprint to avoid needing 'app' for '@app.route'
api_blueprint = Blueprint('api', __name__, template_folder='templates')

# The Home page is accessible to anyone
@api_blueprint.route('/')
def home():
    d = {"status": 401, "message": "No resources here"}
    return jsonify(d)

