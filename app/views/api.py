from flask import Blueprint, jsonify

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