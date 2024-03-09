import unittest
from task import convert_to_binary, convert_binary_to_hexadecimal, conv_endian


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


if __name__ == '__main__':
    unittest.main()
