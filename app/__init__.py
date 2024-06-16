from flask import Flask
import os
from app.config import config
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_caching import Cache

db = SQLAlchemy()
ma = Marshmallow()
cache = Cache()

def create_app():
    app = Flask(__name__)

    config_name = os.getenv('FLASK_ENV') 

    f = config.factory(config_name if config_name else 'development') #seleccciona el modo desarrollo, test o produccion para flask
    app.config.from_object(f) #aca tambien
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DEV_DATABASE_URI') 

    f.init_app(app) #inicia la app con el modo seleccionado
    db.init_app(app)
    ma.init_app(app)

    redis_host = os.getenv('REDIS_HOST')
    redis_password = os.getenv('REDIS_PASSWORD')
    cache.init_app(app, config={'CACHE_TYPE': 'RedisCache', 'CACHE_DEFAULT_TIMEOUT': 300, 'CACHE_REDIS_HOST': redis_host, 'CACHE_REDIS_PORT': '6379', 'CACHE_REDIS_DB': '0', 'CACHE_REDIS_PASSWORD': redis_password, 'CACHE_KEY_PREFIX': 'user_'})

    from app.resources import user
    app.register_blueprint(user, url_prefix='/api/v1/user')

    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app