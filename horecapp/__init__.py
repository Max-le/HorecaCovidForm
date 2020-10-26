from flask import Flask

from . import views

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, instance_relative_config=True)


app.register_blueprint(views.bp)


