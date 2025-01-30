from flask import Flask
from flask_cors import CORS

from app.main.routes import bp as main_bp
from app.db import db
from .config import Config

# Setup flask extensions
cors = CORS()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    cors.init_app(app)

    app.register_blueprint(main_bp)

    return app
