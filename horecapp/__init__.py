from flask import Flask

from . import views

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.logger.info(app.config)
db = SQLAlchemy(app)

app.register_blueprint(views.bp)



class Visitors(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))
    tel_number = db.Column(db.String(128))
    email = db.Column(db.String(128))
    date_visit = db.Column(db.String(128))
    hour_visit = db.Column(db.String(128))
#     place_visited = db.relationship('Horecadmin', backref='visito')


# class Horecadmin(db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     admin_name = db.Column(db.String(128), unique = True, nullable = False)
#     password = db.Column(db.String(1024))
    


app.logger.info("db created.")
db.create_all()
app.logger.info(db)

