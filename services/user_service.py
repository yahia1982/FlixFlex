import hashlib
import os

from dao.user_dao import UserDao

user_dao = UserDao()


def encrypt_password(password):
    salt = os.urandom(32)
    hash_object = hashlib.sha256()
    hash_object.update(salt + password.encode())
    return hash_object.hexdigest()


class UserService:

    def user_exists(self, username):
        user = user_dao.get_user_by_username(username)
        return user is not None

    def register_user(self, username, password):
        if self.user_exists(username):
            return {
                      "status": "error",
                      "message": "Registration failed due duplicate username.",
                      "data": None
                    }, 500
        hashed_password = encrypt_password(password)
        inserted_user = user_dao.create_user(username, hashed_password)
        return {
                  "status": "success",
                  "message": "User successfully registered.",
                  "data": inserted_user
                }, 200
