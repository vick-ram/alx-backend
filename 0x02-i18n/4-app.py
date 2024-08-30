#!/usr/bin/env python3
"""A basic Flask application with Babel support."""

from flask import Flask, render_template, request
from flask_babel import Babel, get_locale

app = Flask(__name__)

# Configure Babel
babel = Babel(app)

# Configuration class


class Config:
    LANGUAGES = ["en", "fr"]
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


@app.route('/')
def index():
    """Renders the index page."""
    return render_template('index.html',
                           home_title=_('home_title'),
                           home_header=_('home_header'))


if __name__ == '__main__':
    app.run(debug=True)
