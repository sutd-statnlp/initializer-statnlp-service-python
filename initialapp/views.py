from initialapp import app
from flask import render_template, send_from_directory


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)