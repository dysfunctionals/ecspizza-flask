import datetime, random

from flask import current_app
from flask_script import Command
from faker import Faker
from .add_users import find_or_create_user
import uuid
from app import db
from app.models.user_models import *
from app.models.pizza_models import *

class MockDataCommand(Command):
    """ Initialize the database."""

    def run(self):
        mock_data()

def mock_data():
    """ Initialize the database."""
    faker = Faker()
    print("Mocking")
    for i in range(1,100):
        print(i)
        user = find_or_create_user(faker.first_name(), faker.last_name(), faker.email(), "Password1")
    db.session.commit()