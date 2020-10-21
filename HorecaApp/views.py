import os

from flask import current_app as app
from flask import render_template, flash, request, redirect, url_for, Blueprint

from HorecaApp.db import get_db


bp = Blueprint('upload', __name__, url_prefix='/')

@bp.route('/answer')
def everything_answer():
    return "42"



@bp.route('/visitors')
def get_list_visitors():
    db = get_db()
    visitors = db.execute('SELECT * FROM visitors').fetchall()
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
        
        db = get_db()

        db.execute('INSERT INTO visitors (first_name, last_name, email, date_visit, hour_visit) VALUES (?, ?, ?, ?, ?)', 
        (first_name, last_name, email, date_visit, hour_visit))

        db.commit()
    


    
    return render_template("form.html")
