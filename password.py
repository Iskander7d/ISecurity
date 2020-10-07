"""
# Фролов Александр Леонидович КЭ-402
"""

from random import choice
from math import ceil

P = 10 ** (-5)
T = 14400  #Дни в минутах
V = 15

low_border = ceil(V * T / P)
pass_len_min = 6
pass_len_max = 12


def create_alphabet():
    start_special = 33
    end_special = 39

    start_numbers = 48
    end_numbers = 57

    start_eng_u = 65
    end_eng_u = 91

    start_eng_l = 97
    end_eng_l = 123

    alph = [chr(index) for index in range(start_special, end_special)]
    alph += [chr(index) for index in range(start_numbers, end_numbers)]
    alph += [chr(index) for index in range(start_eng_u, end_eng_u)]
    alph += [chr(index) for index in range(start_eng_l, end_eng_l)]

    return alph


def generatePassword(border):
    password_len = pass_len_min
    alphabet = create_alphabet()
    while border > (len(alphabet) ** password_len):
        if password_len < pass_len_max:
            password_len += 1
            continue
        if password_len >= pass_len_max:
            exit("Невозможно создать такой пароль.") #Допустим можно увеличить параметр V, или уменьшить максимульную длину пароля, чтобы попасть в этот кейс

    password = ""
    for i in range(password_len):
        password += choice(alphabet)

    return password

print(generatePassword(low_border))