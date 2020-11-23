import os 

from flask import Flask
from flask import render_template, flash, request, redirect, url_for, Blueprint, session
from werkzeug.security import check_password_hash, generate_password_hash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///horecatest.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.logger.info(app.config)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///horecatest.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.logger.info(app.config)

db = SQLAlchemy(app)



class Visitors(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))
    tel_number = db.Column(db.String(128))
    email = db.Column(db.String(128))
    date_visit = db.Column(db.String(128))
    hour_visit = db.Column(db.String(128))
    place_visited = db.relationship('Horecadmin', backref='visito')


class Horecadmin(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    admin_name = db.Column(db.String(128), unique = True, nullable = False)
    password = db.Column(db.String(1024))
    
db.create_all()
app.logger.info("db created.")



@app.route('/answer')
def everything_answer():
    return "42"
@app.route('/')
def show_landing_page():
    return render_template('landing.html')

@app.route('/admin', methods=('GET', 'POST'))
def admin_login():
    if request.method == 'POST':
        admin_name = request.form['adminName']
        passwordTried = request.form['password']
        
        error = None


        ##Security flaw - don't indicate what information is wrong.
        if admin is None:
            error = 'Incorrect username.'
        elif not check_password_hash(admin['password'], passwordTried):
            error = "wrong pwd."



        if error is None:
            session.clear()
            session['user_id'] = admin['id']
            return 'Succesfull admin login !'
        flash(error)
    return render_template('admin.html')



def get_list_visitors():

    for visitor in visitors: 
        print(tuple(visitor))
    return "List of visitors will appear here."


@app.route('/form', methods=['GET', 'POST'])
def provide_form():

    if request.method == "POST": 

        first_name = request.form.get("firstName")
        last_name = request.form.get("lastName")
        email = request.form.get("email")
        date_visit = request.form.get("dateVisit")
        hour_visit = request.form.get("hourVisit")
        return render_template("validated.html")
   
    return render_template("form.html")
