# This file defines command line commands for manage.py
#
# Copyright 2014 SolidBuilds.com. All rights reserved
#
# Authors: Ling Thio <ling.thio@gmail.com>

import datetime

from flask import current_app
from flask_script import Command

from app import db
from app.models.user_models import *
from app.models.pizza_models import *

class MockDataCommand(Command):
    """ Initialize the database."""

    def run(self):
        mock_data()

def mock_data():
    """ Initialize the database."""
    print("Mocking")