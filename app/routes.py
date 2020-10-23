from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from app import app

from app.forms import LoginForm
from app.models import User


@app.route('/')
@app.route('/home')
@login_required
def home():
    students = User.query.all()
    is_holiday = True
    return render_template(
        'index.html',
        students=students,
        is_holiday=is_holiday
    )

@app.route('/login', methods=['GET', 'POST']
def login():

    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None and user.check_password(form.password.data):
            flash("Invalid input data")
            return redirect(url_for("login"))
        login_user(user)
        return redirect(url_for('home'))
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))