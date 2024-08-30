#!/usr/bin/env python3
"""A basic Flask application with Babel support."""
from flask import Flask, render_template, request
from flask_babel import Babel, get_locale


class Config:
    """Configuration class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)


babel = Babel(app)


@babel.localeselector
def get_locale():
    """Determines the best matching locale from the request."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Renders the index page."""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
