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

    binary_num = convert_to_binary(num)
    hex_num = convert_binary_to_hexadecimal(binary_num)

    if endian == 'little':
        hex_values = hex_num.split()  # split into groups so each byte is len 2
        hex_values.reverse()  # reverse the groups
        hex_num = ' '.join(hex_values)

    return hex_num


def convert_to_binary(num):
    """
    helper function to convert an integer number into a binary number.
    Successive division method.

    :param num: an integer (decimal number).
    :returns: binary number as a string.
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


def convert_binary_to_hexadecimal(binary_num):
    """
    helper function to convert a binary number into a hexadecimal number.
    Each byte must be two characters in length.
    The returned string will have each byte separated by a space.

    :param binary_num: a binary number as a string.
    :returns: hexadecimal equivalent as a string.
    """
    decimal_to_hex = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6',
                      7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
                      13: 'D', 14: 'E',  15: 'F'}

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

    add_spaces = ' '.join(string_hex_number[i:i+2]
                          for i in range(0, len(string_hex_number), 2))

    return add_spaces


def my_datetime(num_sec):
    SECONDS_IN_A_DAY = 86400
    days_since_epoch = num_sec // SECONDS_IN_A_DAY

    # Starting vals
    year = 1970
    days_in_year = 365

    # Determine the correct year and adjust days for leap years
    while days_since_epoch >= days_in_year:
        days_since_epoch -= days_in_year
        year += 1
        days_in_year = (
            366 if (year % 4 == 0 and year % 100 != 0)
            or (year % 400 == 0) else 365
        )

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
    return f"{current_month + 1:02d}-{day:02d}-{year}"
