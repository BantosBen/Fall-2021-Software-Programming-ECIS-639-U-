import ex_2_2 as my_module
import hp_1 as hp


def user_list(users):
    user_objects = list()
    account_dict = hp.convert_list(users)
    for account in account_dict:
        user_object = my_module.User(**account)
        user_objects.append(user_object)

    return user_objects
