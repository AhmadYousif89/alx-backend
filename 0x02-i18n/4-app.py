#!/usr/bin/env python3
"""
Basic Flask app with a single route
"""

from flask_babel import Babel
from flask import Flask, render_template, request


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


@app.route('/', methods=['GET'])
def index() -> str:
    """Main page for the Flask app"""
    return render_template('4-index.html', locale=get_locale())


if __name__ == "__main__":
    app.run()
