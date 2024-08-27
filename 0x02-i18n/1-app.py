#!/usr/bin/env python3
"""
Basic Flask app with a single route
"""

from flask_babel import Babel
from flask import Flask, render_template


class Config:
    """Babel i18n configuration"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.url_map.strict_slashes = False
app.config.from_object(Config)
babel = Babel(app)


@app.route('/', methods=['GET'])
def index() -> str:
    """Main page for the Flask app"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()
