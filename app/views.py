"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

import os
from app import app
from flask import render_template, request
from flask_wtf import FlaskForm
from .forms import RegisterForm
from werkzeug.utils import secure_filename
from app import db
from app.models import Users 
from datetime import date

###
# Routing for your application.
###

@app.route('/api/users/register', methods =["POST"])
def register():
    my_register = RegisterForm()
    if request.method =="POST" and my_register.validate_on_submit():
        username = my_register.Username.data
        password = my_register.Password.data
        firstname = my_register.Firstname.data
        lastname = my_register.Lastname.data
        email =  my_register.Email.data
        location = my_register.Location.data
        biography = my_register.biography.data
        Date = joinDate()
        user = Users(username,password,firstname,lastname,email,location,biography,Date)
        db.session.add(user)
        db.session.commit()
        return render_template("index.html")

    form_errors(my_register)
    return render_template('index.html', my_register=my_register)


def joinDate():
    today = day.today().strftime('%B/%d/%Y')



# Please create all new routes and view functions above this route.
# This route is now our catch all route for our VueJS single page
# application.
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    """
    Because we use HTML5 history mode in vue-router we need to configure our
    web server to redirect all routes to index.html. Hence the additional route
    "/<path:path".

    Also we will render the initial webpage and then let VueJS take control.
    """
    return app.send_static_file('index.html')



# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages


###
# The functions below should be applicable to all Flask apps.
###


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
