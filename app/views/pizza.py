from flask import Blueprint, jsonify, request, current_app as app
from flask_user import current_user, login_required, roles_accepted
from flask import Blueprint, render_template
from app import photos
from app.models.pizza_models import PizzaType, Pizza
import uuid
import datetime

# When using a Flask app factory we must use a blueprint to avoid needing 'app' for '@app.route'
pizza_blueprint = Blueprint('pizza', __name__, template_folder='templates')


@pizza_blueprint.route('/upload_test', methods=['GET', 'POST'])
@login_required
def upload_test():
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        return filename
    return render_template('pages/upload_test.html')


@pizza_blueprint.route('/new', methods=['GET', 'POST'])
@login_required
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        pizza_uuid = str(uuid.uuid4())
        pizza_type = request.form['type']
        filename = photos.save(request.files['photo'], name=pizza_uuid + '.')
        return pizza_uuid
    else:
        pizza_types = PizzaType.query.order_by(PizzaType.name).all()
        return render_template('pages/pizza_upload.html', pizza_types=pizza_types)
