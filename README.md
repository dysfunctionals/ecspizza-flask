# ecs.pizza

This is the main Flask app for ecs.pizza

Based on [Flask-User-Starter-App](https://github.com/lingthio/Flask-User-starter-app).

## Installation instructions
- Clone the repo
- Setup a virtualenv
- `pip install -r requirements.txt`
- `cp app/local_settings_example.py app/local_settings.py`
- `python manage.py init_db`
- Now run the dev server: `python manage.py runserver`

## Run the tests
`py.test tests/`
