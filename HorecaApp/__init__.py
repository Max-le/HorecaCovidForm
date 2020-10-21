from flask import Flask
import os
from . import views
from . import db


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, 'horeca.sqlite'),
    )
    app.config.from_pyfile("config.py")
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(views.bp)


    db.init_app(app)

    return app


