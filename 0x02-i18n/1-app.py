#!/usr/bin/env python3
"""
Basic Flask app with a single route
"""

from flask_babel import Babel
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False
babel = Babel(app)


@app.route('/', methods=['GET'])
def index() -> str:
    """Main page for the Flask app"""
    return render_template('1-index.html')


class Config:
    """Babel i18n configuration"""

    LANGUAGES: list[str] = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


if __name__ == "__main__":
    app.run()
