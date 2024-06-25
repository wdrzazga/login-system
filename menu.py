import sys


class MenuLogged:
    def __init__(self, user_):
        self.options = ('Change password', 'Change full name', 'Logout', 'Exit')
        self.selected = None
        self.user = user_

    def print_options(self):
        for i, item in enumerate(self.options):
            print(f'{i+1}. {item}')

    def select_option(self):
        self.selected = input("Choose an option: ")

    def execute_option(self):
        if self.selected == '1' or self.selected == 'Change password':
            self.pick_password()
        elif self.selected == '4' or self.selected == 'Exit':
            sys.exit(0)

    def pick_password(self):
        inputted_old_password = str(input('Type current password: '))
        if inputted_old_password == self.user.password:
            self.user.password = str(input('Type new password: '))


class MenuUnlogged:
    def __init__(self):
        pass
