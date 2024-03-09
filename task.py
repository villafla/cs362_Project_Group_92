"""
Add functions in this file
"""


def conv_num(num_str):
    """
    takes in a string, converts it into a base 10 number, and returns it.

    :param num_str: string representing an integer, float, or hexadecimal
                    number
    :return:        base 10 number of num_str
    """
    vals = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
            '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14,
            'F': 15, 'X': 0, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14,
            'f': 15, 'x': 0}
    int_val = 0
    dec_val = 0
    sign = 1
    is_float = False
    dec_div = 1
    is_hex = False
    exp = len(num_str)-1

    # check for hex or negative hex
    if num_str[0] == '-' and num_str[1] == '0' and (num_str[2] == 'x' or
                                                    num_str[2] == 'X'):
        if len(num_str) == 3:
            return None
        is_hex = True
    if num_str[0] == '0' and (num_str[1] == 'x' or num_str[1] == 'X'):
        if len(num_str) == 2:
            return None
        is_hex = True

    for digit in num_str:
        if digit == '-':
            sign = -1
            exp -= 1
            continue
        if digit == '.':
            if is_float or is_hex:
                return None
            is_float = True
            continue
        if digit.isalpha() and (num_str[0] != '0' or (num_str[1] != 'x' and
                                                      num_str[1] != 'X')):
            return None
        if is_float:
            dec_val = (dec_val * 10) + vals[digit]
            dec_div *= 10
        elif is_hex:
            if digit not in vals:
                return None
            int_val += (16 ** exp) * vals[digit]
            exp -= 1
        else:
            int_val = int_val * 10 + vals[digit]

    if is_float:
        int_val = int_val + (dec_val / dec_div)
    int_val = int_val * sign
    return int_val
