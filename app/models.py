from enum import unique
from sqlalchemy.orm import relationship

from app import db


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True)
    
    def __repr__(self):
        return f"Team - {self.name}"


class Language(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True)
    
    def __repr__(self):
        return f"Language - {self.name}"


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), index=True, unique=True)
    email = db.Column(db.String(100), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    team_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    team = relationship("Team", backref="students")
    
    main_language_id = db.Column(db.Integer, db.ForeignKey('language.id'))
    main_language = relationship("Language", backref="students")

    def __repr__(self):
        return f"User - {self.username}"