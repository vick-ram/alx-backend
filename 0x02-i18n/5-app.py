#!/usr/bin/env python3
"""A basic Flask application with Babel support and user emulation."""

from flask import Flask, render_template, request
from flask_babel import Babel, get_locale

app = Flask(__name__)

babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Configuration class"""
    LANGUAGES = ["en", "fr", "kg"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Determines the best matching locale from the request."""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """Retrieves user data based on the 'login_as' parameter."""
    user_id = request.args.get('login_as')
    if user_id and int(user_id) in users:
        return users[int(user_id)]
    return None


@app.before_request
def before_request():
    """Sets the logged-in user on flask.g.user."""
    flask.g.user = get_user()


@app.route('/')
def index():
    """Renders the index page."""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(debug=True)
