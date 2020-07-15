from ezwashing import app
from ezwashing import machine_status
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html', status=machine_status.status)