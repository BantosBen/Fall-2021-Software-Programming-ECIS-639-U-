def get_addresses(*args):
    ip_list = list()

    for i in range(len(args)):
        arg_list = args[i]
        ip_list.extend(arg_list)

    ip_list = list(set(ip_list))
    return ip_list
