import unittest

from utils import utils


class UtilsTests(unittest.TestCase):
    def test_reversed_integer(self):
        self.assertEqual(utils.reversed(12340), 4321)
        self.assertEqual(utils.reversed(-123), -321)

    def test_reversed_string(self):
        with self.assertRaises(TypeError):
            utils.reversed("123")

    def test_reversed_float(self):
        with self.assertRaises(TypeError):
            utils.reversed(123.0)

    def test_formatter_integer(self):
        self.assertEqual(utils.formatter(10), ("0b1010", "0o12"))

    def test_formatter_string(self):
        with self.assertRaises(TypeError):
            utils.formatter("10")

    def test_formatter_float(self):
        with self.assertRaises(TypeError):
            utils.formatter(10.0)


if __name__ == "__main__":
    unittest.main()
