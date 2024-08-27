#!/usr/bin/env python3
"""
Basic Flask app with a single route
"""

from flask_babel import Babel
from flask import Flask, render_template, request


class Config:
    """Babel i18n configuration"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.url_map.strict_slashes = False
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Get locale"""
    best_match = request.accept_languages.best_match(app.config['LANGUAGES'])
    return best_match if best_match else app.config['BABEL_DEFAULT_LOCALE']


@app.route('/', methods=['GET'])
def index() -> str:
    """Main page for the Flask app"""
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run()
