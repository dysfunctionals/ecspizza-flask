from flask import Blueprint, jsonify, request, current_app as app
from flask_user import current_user, login_required, roles_accepted
from flask import Blueprint, render_template, url_for
from app import photos, db
from app.models.pizza_models import PizzaType, Pizza
import uuid
import datetime

# When using a Flask app factory we must use a blueprint to avoid needing 'app' for '@app.route'
pizza_blueprint = Blueprint('pizza', __name__, template_folder='templates')


@pizza_blueprint.route('/new', methods=['POST'])
@login_required
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        pizza_uuid = str(uuid.uuid4())
        pizza_type_name = request.form['type']
        pizza_type = PizzaType.query.filter_by(slug=pizza_type_name).first_or_404()

        pizza = Pizza(pizza_type_id=pizza_type.id,
                      date_time=datetime.datetime.now(),
                      user_id=current_user.id,
                      uuid=pizza_uuid)

        filename = photos.save(request.files['photo'], name=pizza_uuid + '.jpg')
        db.session.add(pizza)
        db.session.commit()

        STATIC_LOC='/home/kch/Documents/HACK/ecspizza-flask/app'

        from verification.ecspizza_ispizza.verify_pizza import verify
        result = verify(STATIC_LOC + url_for('static', filename='uploads/pizza_img/' + pizza_uuid + '.jpg'))
        verified = False
        category = 'pizza'
        if result == u'🍕':
            verified = True
        else:
            category = result

        return render_template('pages/pizza_verify.html', verified=str(verified), category=category)
