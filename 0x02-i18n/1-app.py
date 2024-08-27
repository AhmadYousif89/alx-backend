#!/usr/bin/env python3
"""
Basic Flask app with a single route
"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
app.url_map.strict_slashes = False
bable = Babel(app)


@app.route('/', methods=['GET'])
def index():
    """Main page for the Flask app"""
    return render_template('1-index.html')


class Config:
    """Babel i18n configuration"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

    def __init__(self):
        """Initialize Config"""
        pass
