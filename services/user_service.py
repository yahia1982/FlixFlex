from dao.user_dao import UserDao

user_dao = UserDao()

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
                    }
        inserted_user = user_dao.create_user(username, password)
        print(inserted_user)

        return {
                  "status": "success",
                  "message": "User successfully registered.",
                  "data": inserted_user
                }
