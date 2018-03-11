from flask import Blueprint, jsonify, current_app as app, request, abort
from app.models.user_models import User, AuthToken
from app import db
import random, string, datetime

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

    if not verified:
        abort(403)

    token_string = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(64))

    token = AuthToken(user_id=user.id,
                      auth_token=token_string,
                      expiry=datetime.datetime.max)

    db.session.add(token)
    db.session.commit()

    d = {
            "status": 200,
            "uuid": user.uuid,
            "token": token.auth_token
    }
    return jsonify(d)

@api_blueprint.route('/userpizzas/<uuid>')
def userpizzas(uuid):
    if not request.headers.has_key("Authorization"):
        abort(403)

    if AuthToken.query.filter_by(auth_token=request.headers.get("Authorization")).count() == 0:
        abort(403)

    user = User.query.filter_by(uuid=uuid).first_or_404()

    d= user.pizzas

    return jsonify(d)