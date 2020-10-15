from flask import render_template, flash, redirect, url_for
from app import app

from app.forms import LoginForm


@app.route('/')
def home():
    students = [
        {'name' : 'Fatima'},
        {'name' : 'Mirelesger'},
        {'name' : 'Ugur'}
    ]
    is_holiday = True
    return render_template(
        'index.html',
        students=students,
        is_holiday=is_holiday
    )

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        msg = f"Username: {form.username.data}, Password: {form.password.data}"
        flash(msg)
        redirect(url_for('home'))
    return render_template('login.html', form=form)