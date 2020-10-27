import os

from flask import current_app as app
from flask import render_template, flash, request, redirect, url_for, Blueprint, session


from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('upload', __name__, url_prefix='/')

@bp.route('/answer')
def everything_answer():
    return "42"



@bp.route('/admin', methods=('GET', 'POST'))
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
    return render_template('admin.html', error=error)



def get_list_visitors():

    for visitor in visitors: 
        print(tuple(visitor))
    return "List of visitors will appear here."


@bp.route('/', methods=['GET', 'POST'])
def provide_form():

    if request.method == "POST": 

        first_name = request.form.get("firstName")
        last_name = request.form.get("lastName")
        email = request.form.get("email")
        date_visit = request.form.get("dateVisit")
        hour_visit = request.form.get("hourVisit")
        return render_template("validated.html")
   
    return render_template("form.html")
