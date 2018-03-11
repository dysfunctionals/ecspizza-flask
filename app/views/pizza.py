from flask import Blueprint, jsonify, request, current_app as app
from flask_user import current_user, login_required, roles_accepted
from flask import Blueprint, render_template
from app import photos, db
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
        pizza_type_name = request.form['type']
        pizza_type = PizzaType.query.filter_by(slug=pizza_type_name).first_or_404()

        pizza = Pizza(pizza_type_id=pizza_type.id,
                      date_time=datetime.datetime.now(),
                      user_id=current_user.id)

        filename = photos.save(request.files['photo'], name=pizza_uuid + '.')
        db.session.add(pizza)
        db.session.commit()
        return pizza_uuid
    else:
        pizza_types = PizzaType.query.order_by(PizzaType.name).all()
        return render_template('pages/pizza_upload.html', pizza_types=pizza_types)
