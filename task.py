import math


def conv_endian(num, endian='big'):
    """
    converts an integer number into a hexadecimal number.
    Each byte must be 2 char in length.
    Handles negative values for num.

    :param num: an integer. can handle negatives.
    :param endian: 'big' for big-endian, 'little' for little-endian
    :returns: hexadecimal number determined by endian flag
    """

    if endian not in ('big', 'little'):
        return None

    is_neg = False
    if num < 0:
        is_neg = True
        num = abs(num)

    binary_num = conv_binary(num)
    hex_num = conv_hex(binary_num)

    if endian == 'little':
        hex_values = hex_num.split()  # split into groups so each byte is len 2
        hex_values.reverse()  # reverse the groups
        hex_num = ' '.join(hex_values)

    if is_neg:
        hex_num = '-' + hex_num

    return hex_num


def conv_binary(num):
    """
    helper function to convert an integer number into a binary number.
    Successive division method.

    :param num: an integer (decimal number).
    :returns: binary number as a string
    """
    binary_number = []

    new_num = abs(num)
    while new_num > 0:
        if new_num % 2 == 0:
            new_num = new_num // 2
            remainder = 0
            binary_number.append(remainder)
        else:
            new_num = new_num // 2
            remainder = 1
            binary_number.append(remainder)

    binary_number = binary_number[::-1]  # reverse the string

    if len(binary_number) % 4 != 0:
        leading_zeros = 4 - (len(binary_number) % 4)
        binary_number = [0] * leading_zeros + binary_number

    # handle negatives
    negative_binary = []
    if num < 0:
        for i in binary_number:
            if i == 1:
                negative_binary.append(0)
            else:
                negative_binary.append(1)
        if negative_binary[len(negative_binary) - 1] == 0:
            negative_binary[len(negative_binary) - 1] = 1   # two's complement
        binary_number = negative_binary

    string_binary_number = ''.join(str(x) for x in binary_number)

    return string_binary_number


def conv_hex(binary_num):
    """
    helper function to convert a binary number into a hexadecimal number.
    Each byte must be two characters in length.
    The returned string will have each byte separated by a space.

    :param binary_num: a binary number as a string.
    :returns: hexadecimal equivalent as a string.
    """
    decimal_to_hex = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6',
                      7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
                      13: 'D', 14: 'E', 15: 'F', -0: '-0', -1: '-1', -2: '-2',
                      -3: '3', -4: '-4', -5: '-5', -6: '-6', -7: '-7',
                      -8: '-8', -9: '-9', -10: '-A', -11: '-B', -12: '-C',
                      -13: '-D', -14: '-E', -15: '-F'}

    if len(binary_num) % 4 != 0:
        leading_zeros = 4 - (len(binary_num) % 4)
        binary_num = '0' * leading_zeros + binary_num

    sections = []
    for i in range(0, len(binary_num), 4):
        section = binary_num[i:i+4]  # slice the string into sections of 4
        sections.append(section)

    totals = []
    for section in sections:
        total_of_subsection = 0
        for j in range(len(section)):
            if section[j] == '1':
                total_of_subsection += 2 ** (3 - j)
        totals.append(total_of_subsection)

    hex_totals = []
    for i in totals:
        hexa = decimal_to_hex[i]
        hex_totals.append(hexa)

    string_hex_number = ''.join(str(x) for x in hex_totals)

    if len(string_hex_number) % 2 != 0:
        leading_zeros = 2 - (len(string_hex_number) % 2)
        string_hex_number = '0' * leading_zeros + string_hex_number

    string_hex_number = ' '.join(string_hex_number[i:i+2]
                                 for i in range(0, len(string_hex_number), 2))

    return string_hex_number


def my_datetime(num_sec):
    """
    Converts the number of seconds since the epoch: January 1st, 1970
    to a date string format MM-DD-YYYY and accounts for leap years.
    This function handles integer and float inputs, rounding down
    floats to the nearest whole number. Only non-negative values are
    accepted.

    :param num_sec: The number of seconds since epoch. Must be a
                    non-negative integer or float.
    :returns: A string representing the date in MM-DD-YYYY format.

    :raises TypeError: If num_sec is not an integer or float
    :raises ValueError: If num_sec is negative

    * Citation for the following function:
    Date: 03/09/24
    Adapted from: https://www.toppr.com/guides/python-guide/examples/python
    -examples/functions/leap-year/python-program-check-leap-year/#:~:text
    =A%20leap%20year%20Python%20is,will%20be%20checked%20with%20400.
    """

    if not isinstance(num_sec, (int, float)):
        raise TypeError("Invalid input: num_sec must be a "
                        "an integer or float")

    if num_sec < 0:
        raise ValueError("Invalid input: num_sec must be a "
                         "non-negative integer")

    num_sec = math.floor(num_sec)

    SECONDS_IN_A_DAY = 86400
    days_since_epoch = num_sec // SECONDS_IN_A_DAY

    year = 1970
    days_in_year = 365

    # Determine the correct year and adjust days for leap years
    while days_since_epoch >= days_in_year:
        days_since_epoch -= days_in_year
        year += 1

        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            days_in_year = 366
        else:
            days_in_year = 365

    # Determine the correct month and day
    days_per_month = [
        31,
        28 +
        (1 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 0),
        31,
        30,
        31,
        30,
        31,
        31,
        30,
        31,
        30,
        31,
    ]
    current_month = 0
    while days_since_epoch >= days_per_month[current_month]:
        days_since_epoch -= days_per_month[current_month]
        current_month += 1

    day = days_since_epoch + 1

    date = f"{current_month + 1:02d}-{day:02d}-{year}"
    return date


def conv_num(num_str):
    """
    takes in a string, converts it into a base 10 number, and returns it.

    :param num_str: string representing an integer, float, or hexadecimal
                    number
    :return:        base 10 number of num_str
    """
    if num_str == '' or type(num_str) is not type(''):
        return None

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
    result = False

    if num_str[0] == '-':
        sign = -1
        exp -= 1
        num_str = num_str[1:]

    if len(num_str) > 1:
        is_hex, result = hex_helper(num_str)

    if is_hex:
        num_str = num_str[2:]
        exp -= 2

    is_float, is_hex, sign, exp, int_val, dec_val, dec_div, result = (
        conv_num_helper(num_str, is_float, is_hex, sign, exp, int_val,
                        dec_val, dec_div, result, vals))

    if result:
        return None

    if is_float:
        int_val = int_val + (dec_val / dec_div)
    int_val = int_val * sign
    return int_val


def hex_helper(num_str):
    """
    Determines if an input is a hexadecimal value (True or False) and if
    that hexadecimal value is a valid input (result)

    :param num_str: string representing an integer, float, or hexadecimal
                    number
    :return:        is_hex (True or False)
                    result (True or False)
    """
    is_hex = False
    result = False
    if len(num_str) >= 3 and num_str[0] == '-' and num_str[1] == '0' and (
                                    num_str[2] == 'x' or num_str[2] == 'X'):
        if len(num_str) == 3:
            result = True
        is_hex = True
    elif num_str[0] == '0' and (num_str[1] == 'x' or num_str[1] == 'X'):
        if len(num_str) == 2:
            result = True
        is_hex = True
    return is_hex, result


def conv_num_helper(num_str, is_float, is_hex, sign, exp, int_val,
                    dec_val, dec_div, result, vals):
    """
    Helper function to convert string of a number to an integer
    """
    for digit in num_str:
        if digit == '-':
            result = True
            break
        if digit == '.':
            if is_float or is_hex:
                result = True
                break
            is_float = True
            continue
        if digit.isalpha() and not is_hex:
            result = True
            break
        if is_float:
            dec_val = (dec_val * 10) + vals[digit]
            dec_div *= 10
        elif is_hex:
            if digit not in vals:
                result = True
                break
            int_val += (16 ** exp) * vals[digit]
            exp -= 1
        else:
            int_val = int_val * 10 + vals[digit]
    return is_float, is_hex, sign, exp, int_val, dec_val, dec_div, result
