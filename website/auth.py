from flask import Blueprint, render_template, request

auth = Blueprint('auth',__name__)

@auth.route('login', method=['GET','POST'])
def login():
    return render_template('login.html')

@auth.route('logout', method=['GET','POST'])
def logout():
    return render_template('logout.html')

@auth.route('sign_up', method=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email =request.form.get('emial')
        firstName = request.form.get('firstName')
        passward1 = request.form.get('passward1')
        passward2 = request.form.get('passward2')
    return render_template('sign_up.html')