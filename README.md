# Procfile

Heroku uses the Procfile to determine how to run/start the app.

type of worker - application server (gunicorn) - file containing the app: name of object in that file 

gunicorn is what's going to actually run the code.

`web: gunicorn`

WSGI : generic name for a python web server interface.

We'll use `wsgi.py` 
