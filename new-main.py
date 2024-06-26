import sys

from menu import MenuLogged
from user import User
from users_io import save_users, load_users

users = load_users()#[User('admin', 'admin', 'Admin Adas')]
option = None


def display_menu():
    print("")
    for menu_option in ('login', 'register', 'exit'):
        print(menu_option)


def get_option():
    return input('Select an option: ')


def register():
    print('\nREGISTERING NEW USER\n')
    username = input('Enter the username: ')
    password = input('Enter the password: ')
    full_name = input('What is your real name: ')

    new_user = User(username, password, full_name)
    users.append(new_user)
    save_users(users)


def execute_option(selected_option):
    if selected_option == '1' or selected_option == 'login':
        login()
    elif selected_option == '2' or selected_option == 'register':
        register()
    elif selected_option == '3' or selected_option == 'exit':
        print('bye!')
        sys.exit()


def second_menu(u):
    second_menu_option = None

    second_menu = MenuLogged(u)

    while second_menu_option != 'Logout' and second_menu_option != '3':
        second_menu.print_options()
        second_menu.select_option()
        second_menu_option = second_menu.selected
        second_menu.execute_option()


def login():
    username = input('Enter the username: ')
    password = input('Enter the password: ')

    for u in users:
        if u.check_login(username, password):
            print(f'hi {u.full_name}')
            second_menu(u)


while option != 'exit' or option != '4':
    display_menu()
    option = get_option()
    execute_option(option)
