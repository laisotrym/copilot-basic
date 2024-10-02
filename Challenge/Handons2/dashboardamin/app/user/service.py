from app.user.repository import UserRepository
from app.user.model import User

# smart logic
class UserService:
    @staticmethod
    def get_all_users():
        return UserRepository.get_all_users()

    @staticmethod
    def get_user_by_id(user_id):
        return UserRepository.get_user_by_id(user_id)

    @staticmethod
    def create_user(data):
        # 1. create user in db
        user = User(username=data['username'], email=data['email'], password=data['password'])
        UserRepository.create_user(user)

        # 2. send email to user

        # 3. audit logs

        return user

    @staticmethod
    def update_user(user_id, data):
        user = UserRepository.get_user_by_id(user_id)
        if user:
            user.username = data['username']
            user.email = data['email']
            user.password = data['password']
            UserRepository.update_user()
        return user

    @staticmethod
    def delete_user(user_id):
        user = UserRepository.get_user_by_id(user_id)
        if user:
            UserRepository.delete_user(user)
        return user