import re
import math

def has_digit(input_string):
    for char in input_string:
        if char.isdigit():
            return True
    return False


def remove_digits(input):
    # Tìm vị trí của kí tự số trong chuỗi
    digit_index = 0
    for i in range(len(input)):
        if input[i].isdigit():
            digit_index = i
            break

    # Loại bỏ kí tự bên phải (nếu có)
    result_string = input[:digit_index]
    return result_string


def remove_suffix(input_string):
    if ("_" not in input_string):
        return remove_digits(input_string)
    out_put = ""
    pattern = r'\d+[ab]'
    out_put = re.sub(pattern, '', input_string)

    input_arr = input_string.split("_")
    if (len(input_arr) > 2):
        input_arr[2] = remove_digits(input_arr[2])
        if len(input_arr[2]) == 0:
            input_arr.pop(2)
    if (has_digit(input_arr[1])):
        input_arr[1] = remove_digits(input_arr[1])
    if len(input_arr[1]) == 0:
        input_arr.pop(1)

    out_put = "_".join(input_arr)
    return out_put


def classifi_by_rules(rules, filename):
    for rule in rules:
        if (len(rule) > 0):
            for rule_val in rule["value"]:
                if rule_val == filename:
                    return rule_val, rule["label"]
    return None


def decimal_to_256(number):
    binary_array = []
    if number == 0:
        binary_array.append(0)
    else:
        while number > 0:
            binary_array.append(number % 256)
            number //= 256
    binary_array.reverse()
    return binary_array


def nearest_square(number):
    if number < 0:
        return None

    lower_square = int(math.sqrt(number))
    higher_square = lower_square + 1

    lower_square_diff = abs(number - lower_square ** 2)
    higher_square_diff = abs(number - higher_square ** 2)

    if lower_square_diff <= higher_square_diff:
        return lower_square ** 2
    else:
        return higher_square ** 2