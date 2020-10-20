from app import db
from app.models import User, Language, Team


class Repo:
    def add_user(self, entity):
        user = User(
            username=entity.username,
            email=entity.email,
            password_hash=entity.password
        )
        db.session.add(user)
        db.session.commit()
        return user

    def get_user(self, id):
        return User.query.get(id)
    
    def update_user(self, id, **params):
        user = User.query.get(id)
        if params.get('username'):
            user.username = params.get('username')
        if params.get('email'):
            user.email = params.get('email')
        if params.get('password_hash'):
            user.password_hash = params.get('password_hash')
        db.session.commit()
        return user
    
    def delete_user(self, id):
        user = User.query.get(id)
        return db.session.delete(user)