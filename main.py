class User:
    def __init__(self, name, password, full_name):
        self.name = name
        self.password = password
        self.full_name = full_name

    def check_login(self, inputted_name: str, inputted_password: str):
        if inputted_password == self.password and inputted_name == self.name:
            return True
        else:
            return False

    def print_hi(self):
        print(f'Hi, {self.full_name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    user1 = User('ja', 'maslo', 'ja ja')

    print("Enter credentials.")
    n = input("username: ")
    p = input("password: ")

    if user1.check_login(n, p):
        user1.print_hi()
    else:
        print('Wrong password or username, pajacu!')
