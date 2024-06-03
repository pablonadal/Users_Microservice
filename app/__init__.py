from flask import Flask
import os
from app.config import config
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)

    config_name = os.getenv('FLASK_ENV') 

    f = config.factory(config_name if config_name else 'development') #seleccciona el modo desarrollo, test o produccion para flask
    app.config.from_object(f) #aca tambien
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DEV_DATABASE_URI') 

    f.init_app(app) #inicia la app con el modo seleccionado
    db.init_app(app)
    ma.init_app(app)

    from app.resources import user
    app.register_blueprint(user, url_prefix='/api/v1/user')

    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app