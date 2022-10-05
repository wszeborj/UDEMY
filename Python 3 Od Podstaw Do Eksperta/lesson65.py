import random


import random

def wylosuj_unikalne_liczby(amount, total_number):
    number_list = []

    while len(number_list) <= amount:
        one = random.randint(1, total_number)
        if one not in number_list:
            number_list.append(one)

    return number_list


print('my function', wylosuj_unikalne_liczby(6, 49))
print('imported function from "random"',random.sample(range(49), 6))
