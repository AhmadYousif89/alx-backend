#!/usr/bin/env python3
"""
Basic Flask app with a single route
"""

from typing import Dict, Union
from flask_babel import Babel
from flask import Flask, render_template, request, g

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """Babel i18n configuration"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.url_map.strict_slashes = False
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Get locale"""
    langs = app.config['LANGUAGES']
    loc = request.args.get('locale')
    def_loc = app.config['BABEL_DEFAULT_LOCALE']
    if loc in langs:
        return request.args.get('locale')
    best_match = request.accept_languages.best_match(langs)
    return best_match if best_match else def_loc


def get_user() -> Union[Dict, None]:
    """Returns a user dictionary or None if the ID cannot be found"""
    login_as = request.args.get('login_as')
    if login_as:
        user_id = int(login_as)
        return users.get(user_id)
    return None


@app.before_request
def before_request():
    """Set user as a global on flask.g.user"""
    g.user = get_user()


@app.route('/', methods=['GET'])
def index() -> str:
    """Main page for the Flask app"""
    return render_template('5-index.html', locale=get_locale(), user=g.user)


if __name__ == "__main__":
    app.run()
