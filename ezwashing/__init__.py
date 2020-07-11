from flask import Flask

app = Flask(__name__)

from ezwashing import routes
