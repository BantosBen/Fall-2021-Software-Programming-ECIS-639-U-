def int_sum(n):
    total = 0
    i=1
    while i<=n:
        total += n
        i += 1
    return total


def odd_sum(n):
    total = 0
    for i in range(n):
        odd_number = 1 + i * 2
        total += odd_number
    return total
