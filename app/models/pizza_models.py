from app import db

class PizzaType(db.Model):
    __tablename__ = 'pizza_types'
    id = db.Column(db.Integer(), primary_key=True)
    slug = db.Column(db.String(50), nullable=False, unique=True)
    name = db.Column(db.String(50), nullable=False)
    pizzas = db.relationship('Pizza', backref="pizza_type", lazy=True)

    def __str__(self):
        return self.name

class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    id = db.Column(db.Integer(), primary_key=True)
    slug = db.Column(db.String(50), nullable=False, unique=True)
    name = db.Column(db.String(50), nullable=False)
    promo_codes = db.relationship('PromoCode', backref='restaurant', lazy=True)
    pizzas = db.relationship('Pizza', backref="restaurant", lazy=True)

class PromoCode(db.Model):
    __tablename__ = 'promo_codes'
    id = db.Column(db.Integer(), primary_key=True)
    restaurant_id = db.Column(db.Integer(), db.ForeignKey('restaurants.id'), nullable=False)
    value = db.Column(db.String(50), nullable=False, server_default='')
    description = db.Column(db.Unicode(255), nullable=False, server_default=u'')
    expiry_date = db.Column(db.Date())

class Pizza(db.Model):
    __tablename__ = 'pizzas'
    id = db.Column(db.Integer(), primary_key=True)
    pizza_type_id = db.Column(db.Integer(), db.ForeignKey('pizza_types.id'), nullable=False)
    restaurant_id = db.Column(db.Integer(), db.ForeignKey('restaurant.id'), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False)

    @staticmethod
    def count_total():
        return Pizza.query.count()

    @staticmethod
    def total_area(): # terms of pi
        return Pizza.count_total() * (14 * 0.5 * 0.0254)**2

    @staticmethod
    def total_radius():
        return Pizza.total_area() ** 0.5