from app import db

class PizzaType(db.Model):
    __tablename__ = 'pizza_types'
    id = db.Column(db.Integer(), primary_key=True)
    slug = db.Column(db.String(50), nullable=False, unique=True)
    name = db.Column(db.String(50), nullable=False)
    pizzas = db.relationship('Pizza', backref="pizza_types", lazy=True)

class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    id = db.Column(db.Integer(), primary_key=True)
    slug = db.Column(db.String(50), nullable=False, unique=True)
    name = db.Column(db.String(50), nullable=False)
    promo_codes = db.relationship('PromoCode', backref='restaurants', lazy=True)

class PromoCode(db.Model):
    __tablename__ = 'promo_codes'
    id = db.Column(db.Integer(), primary_key=True)
    restaurant_id = db.Column(db.Integer(), db.ForeignKey('restaurants.id'), nullable=False)
    value = db.Column(db.String(50), nullable=False, server_default='')
    description = db.Column(db.Unicode(255), nullable=False, server_default=u'')
    expiry_date = db.Column(db.Date())

class Pizza(db.Model):
    __tablename__ = 'pizzas'
    pizza_type_id = db.Column(db.Integer(), db.ForeignKey('pizza_types.id'), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)