# French convert digit numbers into words
from number_to_letter.values import values, values_dizaine, values_on_ten


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


def get_number_level_text(number, level):

    is_singular = number == "un"

    level_values = {
        3: "milliard" if is_singular else "milliards",
        2: "million" if is_singular else "millions",
        1: "mille",
        0: ""
    }

    return level_values[level]


def convert_one_to_three_digits(digits, level):
    letter = ""

    if digits == "":
        return ""

    if digits[0] == "0":
        return convert_one_to_three_digits(digits[1:], level)

    if len(digits) == 3:

        if digits[0] == "1":
            letter = letter + "cent"
        else:
            letter = letter + values[digits[0]] + " cent"

        if digits[1] == "9":
            letter = letter + " " + values_dizaine["8"] + " " + values_on_ten[digits[2]]
        elif digits[1] == "7":
            letter = letter + " " + values_dizaine["6"] + " " + values_on_ten[digits[2]]
        else:
            letter = letter + " " + values_dizaine[digits[1]] + " " + values[digits[2]]

    if len(digits) == 2:
        if digits[0] == "9":
            letter = letter + " " + values_dizaine["8"] + " " + values_on_ten[digits[1]]
        elif digits[0] == "7":
            letter = letter + " " + values_dizaine["6"] + " " + values_on_ten[digits[1]]
        else:
            letter = letter + " " + values_dizaine[digits[0]] + " " + values[digits[2]]

    if len(digits) == 1:
        if digits == "1" and level == 1:
            letter = ""
        else:
            letter = values[digits]

    return letter + " " + get_number_level_text(letter, level) + " "


# TODO : Convert number into letters

def convert_number_to_text(number):
    number_string = str(number)
    number_text = ""

    number_array = separate_digits(number_string)

    number_thousands_level = len(number_array)-1
    counter = 0

    while number_thousands_level >= 0:

        number_text += convert_one_to_three_digits(number_array[counter], number_thousands_level)

        number_thousands_level -= 1
        counter += 1

    return number_text
