#!/usr/bin/env python3
"""A basic Flask application with Babel support."""

from flask import Flask, render_template, request
from flask_babel import Babel, get_locale

app = Flask(__name__)

babel = Babel(app)

class Config:
    """Configuration class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

@babel.localeselector
def get_locale():
    """Determines the best matching locale from the request."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    """Renders the index page."""
    return render_template('3-index.html',
                           home_title=_('home_title'),
                           home_header=_('home_header'))

if __name__ == '__main__':
    app.run(debug=True)
