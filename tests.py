import unittest
from task import (
    convert_to_binary,
    convert_binary_to_hexadecimal,
    conv_endian,
    my_datetime
)
from task import conv_num


class TestCase(unittest.TestCase):
    """
    Class to test functions in task.py
    """

    def test1(self):
        self.assertTrue(True)

    def test2(self):
        """
        Test to check if a decimal number is correcly converted to binary.
        """
        num = 75
        expected = '01001011'
        self.assertEqual(convert_to_binary(num), expected)

    def test3(self):
        """
        Test to check if a decimal number is correcly converted to binary.
        """
        num = 339
        expected = '000101010011'
        self.assertEqual(convert_to_binary(num), expected)

    def test4(self):
        """
        Test to check if a binary number is correctly converted to hexadecimal.
        """
        binary_num = '10110111'
        expected = 'B7'
        self.assertEqual(convert_binary_to_hexadecimal(binary_num), expected)

    def test5(self):
        """
        Test to check if a binary number is correctly converted to hexadecimal.
        """
        binary_num = '11101001000110100010'
        expected = '0E 91 A2'
        self.assertEqual(convert_binary_to_hexadecimal(binary_num), expected)

    def test6(self):
        """
        A test to check if a binary number is converted to hexadecimal
        correctly.
        """
        binary_num = '1011101010'
        expected = '02 EA'
        self.assertEqual(convert_binary_to_hexadecimal(binary_num), expected)

    def test7(self):
        """
        A test to check the binary to hexadecimal conversion.
        """
        binary_num = '1111011111100'
        expected = '1E FC'
        self.assertEqual(convert_binary_to_hexadecimal(binary_num), expected)

    def test8(self):
        """
        A test to check that a big endian number returns the expected value.
        """
        num = 954786
        endian = 'big'
        expected = '0E 91 A2'
        self.assertEqual(conv_endian(num, endian), expected)

    def test9(self):
        """
        a test to convert a decimal number into hexadecimal.
        """
        num = 954786
        expected = '0E 91 A2'
        self.assertEqual(conv_endian(num), expected)

    # def test10(self):
    #     """
    #     Checks for negative numbers.
    #     """
    #     num = -954786
    #     expected = '-0E 91 A2'
    #     self.assertEqual(conv_endian(num), expected)

    def test11(self):
        """
        a test to convert decimal to hexadecimal.
        """
        num = 954786
        endian = 'little'
        expected = 'A2 91 0E'
        self.assertEqual(conv_endian(num, endian), expected)

    def test12(self):
        """
        Test to check if negative decimal numbers can convert to binary.
        """
        num = -5
        expected = '1011'
        self.assertEqual(convert_to_binary(num), expected)

    def test13(self):
        """
        Test to check if conv_endian returns None
        """
        num = -954786
        endian = 'small'
        expected = None
        self.assertEqual(conv_endian(num, endian), expected)

    def my_datetime_test1(self):
        # Check to see if 0 seconds returns the start date
        self.assertEqual(my_datetime(0), '01-01-1970')

    def my_datetime_test2(self):
        # Test a specific date
        self.assertEqual(my_datetime(123456789), '11-29-1973')

    def my_datetime_test3(self):
        # Test for if my_datetime returns correct date with a leap year
        self.assertEqual(my_datetime(201653971200), '02-29-8360')

    def my_datetime_test4(self):
        # Test for future date
        self.assertEqual(my_datetime(9876543210), '12-22-2282')

    def my_datetime_test5(self):
        # Test for non leap year
        self.assertEqual(my_datetime(34128000), '02-28-1971')

    def test_conv_num_1(self):
        """
        Test to check if a string entry of a positive number correctly
        converts to Base 10.
        """
        num = '54321'
        expected = 54321
        self.assertEqual(conv_num(num), expected)

    def test_conv_num_2(self):
        """
        Test to check if a string entry of a negative number correctly
        converts to Base 10.
        """
        num = '-54321'
        expected = -54321
        self.assertEqual(conv_num(num), expected)

    def test_conv_num_3(self):
        """
        Test to check if a string entry of a positive float number correctly
        converts to Base 10.
        """
        num = '543.21'
        expected = 543.21
        self.assertEqual(conv_num(num), expected)

    def test_conv_num_4(self):
        """
        Test to check if a string entry of a negative float number correctly
        converts to Base 10.
        """
        num = '-543.21'
        expected = -543.21
        self.assertEqual(conv_num(num), expected)

    def test_conv_num_5(self):
        """
        Test to check if a string entry of a positive float number with
        no trailing decimals correctly converts to Base 10.
        """
        num = '543.'
        expected = 543.0
        self.assertEqual(conv_num(num), expected)

    def test_conv_num_6(self):
        """
        Test to check if a string entry of a negative float number with
        no trailing decimals correctly converts to Base 10.
        """
        num = '-543.'
        expected = -543.0
        self.assertEqual(conv_num(num), expected)

    def test_conv_num_7(self):
        """
        Test to check if a string entry of a positive float number with
        only decimal places correctly converts to Base 10.
        """
        num = '.543'
        expected = .543
        self.assertEqual(conv_num(num), expected)

    def test_conv_num_8(self):
        """
        Test to check if a string entry of a negative float number with
        only decimal places correctly converts to Base 10.
        """
        num = '-.543'
        expected = -.543
        self.assertEqual(conv_num(num), expected)

    def test_conv_num_9(self):
        """
        Test to check if a string entry of a positive hexadecimal number
        correctly converts to Base 10.
        """
        num = '0xBA6'
        expected = 2982
        self.assertEqual(conv_num(num), expected)

    def test_conv_num_10(self):
        """
        Test to check if a string entry of a negative hexadecimal number
        correctly converts to Base 10.
        """
        num = '-0xBA6'
        expected = -2982
        self.assertEqual(conv_num(num), expected)

    def test_conv_num_11(self):
        """
        Test to check if a string entry of a positive hexadecimal number
        with lower case letters correctly converts to Base 10.
        """
        num = '0xba6'
        expected = 2982
        self.assertEqual(conv_num(num), expected)

    def test_conv_num_12(self):
        """
        Test to check if a string entry of a negative hexadecimal number
        with lower case letters correctly converts to Base 10.
        """
        num = '-0xba6'
        expected = -2982
        self.assertEqual(conv_num(num), expected)

    def test_conv_num_13(self):
        """
        Test to check if a string entry of a positive hexadecimal number
        with an incorrect letter correctly returns None.
        """
        num = '0xZA6'
        expected = None
        self.assertEqual(conv_num(num), expected)

    def test_conv_num_14(self):
        """
        Test to check if a string entry of a negative hexadecimal number
        with an incorrect letter correctly returns None.
        """
        num = '-0xZA6'
        expected = None
        self.assertEqual(conv_num(num), expected)

    def test_conv_num_15(self):
        """
        Test to check if a string entry of a positive hexadecimal number
        with an incorrect lower case letter correctly returns None.
        """
        num = '0xza6'
        expected = None
        self.assertEqual(conv_num(num), expected)

    def test_conv_num_16(self):
        """
        Test to check if a string entry of a negative hexadecimal number
        with an incorrect lower case letter correctly returns None.
        """
        num = '-0xza6'
        expected = None
        self.assertEqual(conv_num(num), expected)

    def test_conv_num_17(self):
        """
        Test to check if a string entry of a positive, non-hexadecimal number
        with a letter in it correctly returns None.
        """
        num = '54321A'
        expected = None
        self.assertEqual(conv_num(num), expected)

    def test_conv_num_18(self):
        """
        Test to check if a string entry of a negative, non-hexadecimal number
        with a letter in it correctly returns None.
        """
        num = '-54321A'
        expected = None
        self.assertEqual(conv_num(num), expected)

    def test_conv_num_19(self):
        """
        Test to check if a string entry of a positive number
        with more than one decimal in it correctly returns None.
        """
        num = '54.32.1'
        expected = None
        self.assertEqual(conv_num(num), expected)

    def test_conv_num_20(self):
        """
        Test to check if a string entry of a negative number
        with more than one decimal in it correctly returns None.
        """
        num = '-54.32.1'
        expected = None
        self.assertEqual(conv_num(num), expected)

    def test_conv_num_21(self):
        """
        Test to check if a string entry of a positive number
        with more than one decimal in it correctly returns None.
        """
        num = '54.32.1'
        expected = None
        self.assertEqual(conv_num(num), expected)

    def test_conv_num_22(self):
        """
        Test to check if a string entry of a number
        with more than one decimal in it placed a the end
        correctly returns None.
        """
        num = '54.321.'
        expected = None
        self.assertEqual(conv_num(num), expected)

    def test_conv_num_23(self):
        """
        Test to check if a string entry of a positive float number
        with a letter in the decimal place correctly returns None.
        """
        num = '12.B'
        expected = None
        self.assertEqual(conv_num(num), expected)

    def test_conv_num_24(self):
        """
        Test to check if a string entry of a negative float number
        with a letter in the decimal place correctly returns None.
        """
        num = '-12.B'
        expected = None
        self.assertEqual(conv_num(num), expected)

    def test_conv_num_25(self):
        """
        Test to check if a string entry of a positive hexadecimal number
        with a decimal place correctly returns None.
        """
        num = '0xBA6.7'
        expected = None
        self.assertEqual(conv_num(num), expected)

    def test_conv_num_26(self):
        """
        Test to check if a string entry of a negative hexadecimal number
        with a decimal place correctly returns None.
        """
        num = '-0xBA6.7'
        expected = None
        self.assertEqual(conv_num(num), expected)

    def test_conv_num_27(self):
        """
        Test to check if a non-string correctly returns None.
        """
        num = 54321
        expected = None
        self.assertEqual(conv_num(num), expected)

    def test_conv_num_28(self):
        """
        Test to check if an empty string entry correctly returns None.
        """
        num = ''
        expected = None
        self.assertEqual(conv_num(num), expected)

    def test_conv_num_29(self):
        """
        Test to check if a string entry of a positive hexadecimal number
        with '0x' missing at the start correctly returns None.
        """
        num = 'BA6'
        expected = None
        self.assertEqual(conv_num(num), expected)

    def test_conv_num_30(self):
        """
        Test to check if a string entry of a negative hexadecimal number
        with '0x' missing at the start correctly returns None.
        """
        num = '-BA6'
        expected = None
        self.assertEqual(conv_num(num), expected)


if __name__ == '__main__':
    unittest.main()
