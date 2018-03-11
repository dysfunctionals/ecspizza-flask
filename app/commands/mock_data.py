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
        for j in range(0, random.randint(0, 15)):
            pizza = Pizza(
                date_time=faker.past_datetime(start_date="-30d", tzinfo=None),
                pizza_type_id=random.randint(1,6),
                restaurant_id=random.randint(1,9),
                uuid=str(uuid.uuid4()),
                user_id=i
            )
            db.session.add(pizza)
    db.session.commit()
