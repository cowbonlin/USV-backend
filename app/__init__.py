from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api

from config import config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name='default'):
    app = Flask(__name__, instance_relative_config=True)
    
    app.config.from_pyfile('config.py')
    app.config.from_object(config[config_name])
    # config_name: development, test, production

    db.init_app(app)
    migrate.init_app(app, db)

    from app.apis import add_all_resources
    api = Api()
    add_all_resources(api)
    api.init_app(app)

    from .views import api_bp
    app.register_blueprint(api_bp)
    return app
