import os

from flask import current_app as app
from flask import render_template, flash, request, redirect, url_for, Blueprint, session


from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('upload', __name__, url_prefix='/')

@bp.route('/answer')
def everything_answer():
    return "42"
@bp.route('/')
def show_landing_page():
    return render_template('landing.html')

@bp.route('/signup', methods=['POST'])
def admin_signup():
    admin_name = request.form.get('adminName')
    password = request.form.get('password')

    admin = Horecadmin.query.filter_by(admin_name=admin_name).first() # if this returns a user, then the name already exists in database
    if admin:
        return redirect(url_for('signup'))
    new_horeca_admin = Horecadmin(admin_name=admin_name, password=generate_password_hash(password, method='sha256'))
    db.session.add()
    db.session.commit()
    return redirect(url_for('login'))


@bp.route('/login', methods=('GET', 'POST'))
def admin_login():
    if request.method == 'POST':
        admin = request.form['adminName']
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


@bp.route('/form', methods=['GET', 'POST'])
def provide_form():

    if request.method == "POST": 

        first_name = request.form.get("firstName")
        last_name = request.form.get("lastName")
        email = request.form.get("email")
        date_visit = request.form.get("dateVisit")
        hour_visit = request.form.get("hourVisit")
        return render_template("validated.html")
   
    return render_template("form.html")
