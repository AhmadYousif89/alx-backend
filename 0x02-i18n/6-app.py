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
    def_loc = app.config['BABEL_DEFAULT_LOCALE']
    # 1. Locale from URL parameters
    loc = request.args.get('locale')
    if loc in langs:
        return loc
    # 2. Locale from user settings
    if g.user:
        user_locale = g.user.get('locale')
        if user_locale and user_locale in langs:
            return user_locale
    # 3. Locale from request header
    best_match = request.accept_languages.best_match(langs)
    if best_match:
        return best_match
    # 4. Default locale
    return def_loc


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
    return render_template('6-index.html', locale=get_locale(), user=g.user)


if __name__ == "__main__":
    app.run(debug=True)
