from collections import namedtuple


def user_list(users):
    user = namedtuple('User', ['first_name', 'last_name', 'email', 'login_count', 'last_login'])
    users_namedtuple = [user(*user_rec) for user_rec in users]
    return users_namedtuple
