from flask import Blueprint, redirect, render_template
from flask import request, url_for
from flask_user import current_user, login_required, roles_accepted

from app import db
from app.models.user_models import UserProfileForm, User
from app.models.pizza_models import Pizza, PizzaType, Restaurant

# When using a Flask app factory we must use a blueprint to avoid needing 'app' for '@app.route'
main_blueprint = Blueprint('main', __name__, template_folder='templates')


# The Home page is accessible to anyone
@main_blueprint.route('/')
@login_required
def home():
    pizza_types = PizzaType.query.order_by(PizzaType.name).all()
    restaurants = Restaurant.query.order_by(Restaurant.name).all()
    pizzas = Pizza.query.filter_by(user_id=current_user.id).all()
    return render_template('pages/home.html', pizza_types=pizza_types,pizzas=pizzas,restaurants=restaurants)


@main_blueprint.route('/leaderboard')
@login_required
def leaderboard():

    query = "SELECT user_id, COUNT(*) AS amount FROM pizzas GROUP BY user_id ORDER BY amount DESC"
    result = db.engine.execute(query)

    data = []

    for row in result:
        user = User.query.get(row.user_id)
        data.append({"name": user.first_name + " " + user.last_name, "amount": row.amount})

    return render_template('pages/leaderboard.html', data=data)


# The Admin page is accessible to users with the 'admin' role
@main_blueprint.route('/admin')
@roles_accepted('admin')  # Limits access to users with the 'admin' role
def admin_page():
    return render_template('pages/admin_page.html')


@main_blueprint.route('/pages/profile')
@login_required
def user_profile_page():
    return render_template('pages/user_profile_page.html')

@main_blueprint.route('/stats',)
@login_required
def stats():
    radius = Pizza.total_radius()
    return render_template('pages/stats.html', radius=radius)