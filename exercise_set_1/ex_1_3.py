import ex_1_2 as my_module


def last_logins(forms):
    output_dictionary = dict()
    for i in range(len(forms)):
        form = forms[i]
        username, last_login = my_module.last_user_login(form)
        output_dictionary.update({username: last_login})
    return output_dictionary
