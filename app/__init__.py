from flask import Flask
import os
from app.config import config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def createapp():
    app = Flask(__name__)

    config_name = os.getenv('FLASK_ENV')

    f = config.factory(config_name if config_name else 'development')
    app.config.from_object(f)

    f.init_app(app)
    db.init_app(app)

    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app