#!/usr/bin/env python3
"""
Basic Flask app with a single route
"""

from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/', methods=['GET'])
def index():
    """Main page for the Flask app"""
    return render_template('0-index.html')
