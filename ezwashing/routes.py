from ezwashing import app
from ezwashing import machine_status
from flask import render_template

@app.route('/')
def index():
    status = machine_status.get_machine_status()
    return render_template('index.html', status=status)