from flask import render_template
from app import app

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
    