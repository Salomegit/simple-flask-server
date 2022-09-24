from flask import Flask
from . import views as v

def create_app():
    app = Flask(__name__)

    app.register_blueprint(v.auth)

    return app
