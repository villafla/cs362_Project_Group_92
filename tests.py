import unittest
from task import conv_binary, conv_hex, conv_endian
from task import (
    convert_to_binary,
    convert_binary_to_hexadecimal,
    conv_endian,
    my_datetime
)


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
        self.assertEqual(conv_binary(num), expected)

    def test3(self):
        """
        Test to check if a decimal number is correcly converted to binary.
        """
        num = 339
        expected = '000101010011'
        self.assertEqual(conv_binary(num), expected)

    def test4(self):
        """
        Test to check if a binary number is correctly converted to hexadecimal.
        """
        binary_num = '10110111'
        expected = 'B7'
        self.assertEqual(conv_hex(binary_num), expected)

    def test5(self):
        """
        Test to check if a binary number is correctly converted to hexadecimal.
        """
        binary_num = '11101001000110100010'
        expected = '0E 91 A2'
        self.assertEqual(conv_hex(binary_num), expected)

    def test6(self):
        """
        A test to check if a binary number is converted to hexadecimal
        correctly.
        """
        binary_num = '1011101010'
        expected = '02 EA'
        self.assertEqual(conv_hex(binary_num), expected)

    def test7(self):
        """
        A test to check the binary to hexadecimal conversion.
        """
        binary_num = '1111011111100'
        expected = '1E FC'
        self.assertEqual(conv_hex(binary_num), expected)

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

    def test10(self):
        """
        Checks for negative numbers.
        """
        num = -954786
        expected = '-0E 91 A2'
        self.assertEqual(conv_endian(num), expected)

    def test11(self):
        """
        Test to convert decimal to hexadecimal.
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
        self.assertEqual(conv_binary(num), expected)

    def test13(self):
        """
        Test to check if conv_endian returns None
        """
        num = -954786
        endian = 'small'
        expected = None
        self.assertEqual(conv_endian(num, endian), expected)

    def test14(self):
        """
        Test to check a negative number and little endian
        """
        num = -954786
        endian = 'little'
        expected = '-A2 91 0E'
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


if __name__ == '__main__':
    unittest.main()
