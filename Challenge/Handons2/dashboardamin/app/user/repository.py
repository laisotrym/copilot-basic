from app import db
from app.user.model import User

# dummy
class UserRepository:
    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def create_user(user):
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def update_user():
        db.session.commit()

    @staticmethod
    def delete_user(user):
        db.session.delete(user)
        db.session.commit()

    @classmethod
    def get_user_by_email(cls, email):
        return User.query.filter_by(email=email).first()