import unittest

from number_to_letter.utils import separate_digits


class MainTest(unittest.TestCase):

    def separate_digits_test(self):
        self.assertEqual(separate_digits(10000), ['10', '000'])


if __name__ == '__main__':
    unittest.main()
