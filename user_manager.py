import pickle


class UserManager:
    users = []  # [User('admin', 'admin', 'Admin Adas')]
    filename = "usr.dat"

    @staticmethod
    def save_users():
        with open(UserManager.filename, "wb") as file:
            pickle.dump(UserManager.users, file)

    @staticmethod
    def load_users():
        try:
            with open(UserManager.filename, 'rb') as f:
                UserManager.users = pickle.load(f)
        except FileNotFoundError:
            print(f"File {UserManager.filename} not found")
        except Exception as e:
            print(f"An error occurred: {e}")
