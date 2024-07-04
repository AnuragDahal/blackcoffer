# core/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from .config import Config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = Config.DATABASE_URL

    db.init_app(app)

    from core.apis.trigger import trigger
    from core.apis.admin.dashboard import admin_dashboard

    app.register_blueprint(admin_dashboard, url_prefix='/admin')
    app.register_blueprint(trigger)
    CORS(app, origins="*", allow_headers="*")

    @app.route('/', methods=['GET'])
    def status():
        return {"status": "success"}

    return app
