from flask import render_template, redirect, url_for, flash, session
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.forms import LoginForm
from app.models import User
from app.queries import get_user
from cfg import sqlsessionclass, db
from . import auth

@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    context = {
        'login_form' : login_form
    }
    username = login_form.username.data
    password = login_form.password.data

    if current_user.is_authenticated:
        return redirect(url_for('index'))

    if login_form.validate_on_submit():

        user = get_user(username)
        if user:

            if check_password_hash(user.password, password):
                login_user(user)
                flash('Bienvenido de nuevo!', 'alert alert-success alert-dismissible')

                return redirect(url_for('hello'))

            else:
                flash('La información no coincide', 'alert alert-danger')
        else:
            flash('El usuario no existe.', 'alert alert-danger')


        return redirect(url_for('index'))
    
    return render_template('login.html', **context)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    signup_form = LoginForm()
    context = {
        'signup_form' : signup_form
    }
    
    if signup_form.validate_on_submit():
        username = signup_form.username.data
        password = signup_form.password.data

        registered_user = get_user(username)

        if registered_user:
            flash('Ese nombre de usuario está ocupado')
        else:
            password_hash = generate_password_hash(password)
            user = User(username=username,
                        password=password_hash)
            sqlsession = sqlsessionclass()
            sqlsession.add(user)
            sqlsession.commit()
            login_user(user)

            flash('Bienvenido!')

            return redirect(url_for('hello'))
            

    return render_template('signup.html', **context)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Adios!')

    return redirect(url_for('auth.login'))
