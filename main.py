import sys
from user import User
from menu import MenuLogged, MenuUnlogged

if __name__ == '__main__':
    user1 = User('j', 'j', 'ja ja')

    print("Enter credentials.")
    n = input("username: ")
    p = input("password: ")

    if user1.check_login(n, p):
        m = MenuLogged(user1)
        while m.loop:
            user1.print_hi()

            m.print_options()
            m.select_option()
            m.execute_option()
    else:
        print('Wrong password or username, pajacu!')
        m = MenuUnlogged()
        sys.exit()
