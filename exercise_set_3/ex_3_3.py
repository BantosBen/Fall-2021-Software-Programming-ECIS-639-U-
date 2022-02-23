from collections import Counter


def top_3_ips(*args):
    ip_list = list()

    for i in range(len(args)):
        args_list = args[i]
        ip_list.extend(args_list)

    ip_count = Counter(ip_list)
    ip_common_list = list()

    for ip_tup in ip_count.most_common(3):
        ip_common_list.append(ip_tup[0])

    return ip_common_list
