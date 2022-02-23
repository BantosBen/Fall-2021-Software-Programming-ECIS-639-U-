from pathlib import Path
from ex_3_2 import get_addresses

ip_list = list()
with Path('./ip_log.txt').open(mode='r') as reader_obj:
    for line in reader_obj:
        ip_list.append(line)

unique_ip_list = get_addresses(ip_list)
print(len(unique_ip_list))
