import ex_1_1 as my_module


def last_user_login(form):
    email = form[2]
    username = my_module.get_username(email)
    last_login = form[3]
    return username, last_login
