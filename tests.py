import unittest
from task import conv_num


class TestCase(unittest.TestCase):

    def test1(self):
        self.assertTrue(True)

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
