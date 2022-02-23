def filter_positive_even(integers):
    positive_even_integers = list()
    for number in integers:
        if is_positive_even_num(number):
            positive_even_integers.append(number)

    return positive_even_integers


def is_positive_even_num(num):
    rem = num % 2
    return rem == 0 and num
