# French convert digit numbers into words
from values import values, values_dizaine, values_on_ten


def separate_digits(digits):
    reversed_digits = str(digits)[::-1]
    value_array_of_three_digits = []

    i = 0

    stop = False

    while not stop:
        value_array_of_three_digits.append(reversed_digits[i:i + 3])

        last_index = len(value_array_of_three_digits) - 1

        if len(value_array_of_three_digits[last_index]) < 3:
            stop = True

        i = i + 3

    return [element[::-1] for element in value_array_of_three_digits][::-1]


def convert_one_to_three_digits(digits):
    letter = ""

    if len(digits) == 3:
        if digits[0] == "1":
            letter = letter + "cent"
        else:
            letter = letter + values[digits[0]] + " cent"

        if digits[1] == "9":
            letter = letter + " " + values_dizaine["8"] + " " + values_on_ten[digits[2]]
        if digits[1] == "7":
            letter = letter + " " + values_dizaine["6"] + " " + values_on_ten[digits[2]]

    if len(digits) == 2:
        if digits[0] == "9":
            letter = letter + " " + values_dizaine["8"] + " " + values_on_ten[digits[1]]
        if digits[0] == "7":
            letter = letter + " " + values_dizaine["6"] + " " + values_on_ten[digits[1]]

    if len(digits) == 1:
        letter = values[digits]

    return letter

# TODO : Convert number into letters

