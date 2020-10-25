from . import db


class Visitors(db.Model):

    #Columns
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.String(128)
    last_name = db.String(128)
