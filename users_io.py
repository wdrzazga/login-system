import pickle

filename = "usr.dat"


def save_users(users):
    with open(filename, "wb") as file:
        pickle.dump(users, file)


def load_users():
    try:
        with open(filename, 'rb') as f:
            data = pickle.load(f)
            return data
    except FileNotFoundError:
        print(f"File {filename} not found")
    except Exception as e:
        print(f"An error occurred: {e}")
