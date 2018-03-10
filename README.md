# ecs.pizza

[![CircleCI](https://circleci.com/gh/dysfunctionals/ecspizza-flask/tree/master.svg?style=svg)](https://circleci.com/gh/dysfunctionals/ecspizza-flask/tree/master)

This is the main Flask app for ecs.pizza

Based on [Flask-User-Starter-App](https://github.com/lingthio/Flask-User-starter-app).

## Installation instructions
- Clone the repo
- Setup a virtualenv
- `pip install -r requirements.txt`
- `cp app/local_settings_example.py app/local_settings.py`
- `python manage.py init_db`
- `python manage.py add_restaurants`
- To add test users:
    - `python manage.py add_users`
    - Test User: member@example.com , Password1
    - Test Admin: admin@example.com , Password1
- Now run the dev server: `python manage.py runserver`

**Note: registration sends a verification email, so you must have Flask mail sending configured for that to work.**

## Run the tests
`py.test tests/`
