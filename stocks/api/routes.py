from stocks.api import app, db
from flask import render_template, request, redirect, url_for
from stocks.api.forms import UserLoginForm
from stocks.api.models import User

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    form = UserLoginForm()

    try:
        if request.method == 'POST' and form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            print(email, password)

            user = User(email, password = password)

            db.session.add(user)
            db.session.commit()

            return redirect(url_for('signin'))
    except:
        raise Exception('Invalid For Data: Please Check your form')

    return render_template('signup.html', form=form)
    
@app.route('/signin', methods = ['GET', 'POST'])
def signin():
    form = UserLoginForm()
    try:
        if request.method == 'POST' and form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            print(email,password)

    except:
        raise Exception('Invalid Form Data: Please Check Your Form')

    return render_template('signin.html', form=form)