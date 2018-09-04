from flask import Flask

from Formapp import settings
from Formapp.ext import init_ext


def create_app():
    app = Flask(__name__)
    init_ext(app)
    app.config['SECRET_KEY'] = 'abcxyz'
    return app