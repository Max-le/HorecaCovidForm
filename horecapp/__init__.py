from flask import Flask

from . import views

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, instance_relative_config=True)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

app.register_blueprint(views.bp)

db = SQLAlchemy(app)



class Visitors(db.Model):

    #Columns

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))
    tel_number = db.Column(db.String(128))
    email = db.Column(db.String(128))
    date_visit = db.Column(db.String(128))
    hour_visit = db.Column(db.String(128))



class eatery_admin(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    admin_name = db.Column(db.String(128), unique = True, nullable = False)
    password = db.Column(db.String(1024))


print("db created.")
db.create_all()
print(db)

