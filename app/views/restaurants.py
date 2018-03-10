from flask import Blueprint, jsonify
from flask_user import current_user, login_required, roles_accepted
from flask import Blueprint, redirect, render_template
from app.models.pizza_models import Restaurant

# When using a Flask app factory we must use a blueprint to avoid needing 'app' for '@app.route'
restaurants_blueprint = Blueprint('restaurants', __name__, template_folder='templates')

@restaurants_blueprint.route('/')
@login_required
def index():
    restaurants = Restaurant.query.all()
    return render_template('pages/restaurants/index.html',restaurants=restaurants);