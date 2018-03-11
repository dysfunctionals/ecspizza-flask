from flask import Blueprint, jsonify
from flask_user import current_user, login_required, roles_accepted
from flask import Blueprint, redirect, render_template
from app.models.pizza_models import Restaurant, PromoCode

# When using a Flask app factory we must use a blueprint to avoid needing 'app' for '@app.route'
restaurants_blueprint = Blueprint('restaurants', __name__, template_folder='templates')

@restaurants_blueprint.route('/')
@login_required
def index():
    restaurants = Restaurant.query.all()
    return render_template('pages/restaurants/index.html',restaurants=restaurants);

@restaurants_blueprint.route('/<slug>')
@login_required
def view(slug):
    restaurant = Restaurant.query.filter_by(slug=slug).first_or_404()
    promo_count = PromoCode.query.filter_by(restaurant_id=restaurant.id).count()
    return render_template('pages/restaurants/view.html', restaurant=restaurant, promo_count=promo_count);