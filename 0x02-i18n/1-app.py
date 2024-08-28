#!/usr/bin/env python3
"""1-app module"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """Config class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


ap.config.from_object(Config)

babel = Babel(app)


@app.route('/')
def index():
    """routing endpoint"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
