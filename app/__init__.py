from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate

from config import Config

db = SQLAlchemy()
migrate = Migrate()


app = None


def create_app(config_class=Config):
    global app
    if app:
        return app
    app = Flask(__name__, template_folder='templates')
    CORS(app)
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app, db)

    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/v1')

    return app
