import datetime
import uuid

from flask import current_app
from flask_script import Command

from app import db
from app.models.pizza_models import Restaurant

class AddRestaurantsCommand(Command):
    def run(self):
        create_restaurants()

def create_restaurants():
    """ Populates restaurants """

    add_restaurant("Pizzazz Pizza","pizzazz")
    add_restaurant("Dominos","dominos")
    add_restaurant("Pizza Hut","pizzahut")
    # Save to DB
    db.session.commit()

def add_restaurant(name,slug):
    restaurant = Restaurant(name=name, slug=slug)
    db.session.add(restaurant)