from flask import render_template,request,redirect,url_for,abort,flash
from . import auth
from flask_login import login_user,logout_user,login_required,current_user
from ..models import Post,User
from werkzeug.security import generate_password_hash, check_password_hash
from .forms import LoginForm,RegistrationForm
from .. import db


@auth.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username = form.username.data, email = form.email.data, password = form.password.data)
        db.session.add(user)
        db.session.commit()

        mail_message = ("Welcome to PizzaHub","email/welcome_user",user.email)

        return redirect(url_for('auth.login'))
        title = "New Account"
    return render_template('auth/register.html',form = form)

@auth.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    title = "PIZZA-HUB login"
    return render_template('auth/login.html',form = form,title=title)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been successfully logged out')
    return redirect(url_for("main.index"))

