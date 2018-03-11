import datetime
import uuid

from flask import current_app
from flask_script import Command

from app import db
from app.models.pizza_models import Restaurant, PizzaType

class AddRestaurantsCommand(Command):
    def run(self):
        create_restaurants()
        create_pizza_types()


def create_pizza_types():
    """"Populate Pizza Types"""

    add_pizza_type("Cheese and Tomato","cheeseandtomato")
    add_pizza_type("Pepperoni","pepperoni")
    add_pizza_type("Pepperoni Hot","pepperonihot")
    add_pizza_type("Veggi Supreme","veggi")
    add_pizza_type("Meat Feast","meatfeast")
    add_pizza_type("Hawaiian","hawaiian")

    db.session.commit()

def add_pizza_type(name,slug):
    pizza_type = PizzaType(name=name, slug=slug)
    db.session.add(pizza_type)

def create_restaurants():
    """ Populates restaurants """

    add_restaurant("Pizzazz Pizza", "pizzazz")
    add_restaurant("Domino's", "dominos")
    add_restaurant("Pizza Hut", "pizzahut")
    add_restaurant("Uni Kebab", "unikebab")
    add_restaurant("Smokey Pizza", "smokeypizza")
    add_restaurant("Portobello Pizza", "portobello")
    add_restaurant("Baffi Pizza", "baffi")
    add_restaurant("Pizza 2 U", "pizza2u")
    add_restaurant("Pizza Hot 4 U", "pizzahot4u")
    # Save to DB
    db.session.commit()

def add_restaurant(name,slug):
    restaurant = Restaurant(name=name, slug=slug)
    db.session.add(restaurant)