# Copyright 2014 SolidBuilds.com. All rights reserved
#
# Authors: Ling Thio <ling.thio@gmail.com>


from flask import Blueprint, redirect, render_template
from flask import request, url_for
from flask_user import current_user, login_required, roles_accepted

from app import db
from app.models.user_models import UserProfileForm

# When using a Flask app factory we must use a blueprint to avoid needing 'app' for '@app.route'
main_blueprint = Blueprint('main', __name__, template_folder='templates')

# The Home page is accessible to anyone
@main_blueprint.route('/')
@login_required
def home():
    return render_template('pages/home.html')

@main_blueprint.route('/leaderboard')
@login_required
def leaderboard():
    return render_template('pages/leaderboard.html')


# The Admin page is accessible to users with the 'admin' role
@main_blueprint.route('/admin')
@roles_accepted('admin')  # Limits access to users with the 'admin' role
def admin_page():
    return render_template('pages/admin_page.html')


@main_blueprint.route('/pages/profile', methods=['GET'])
@login_required
def user_profile_page():
    return render_template('pages/user_profile_page.html')
