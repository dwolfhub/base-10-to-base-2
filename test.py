import unittest
from base_10_to_base_2 import convert


class TestConvert(unittest.TestCase):
    def test_convert(self):
        self.assertEqual(False, convert(-1))
        self.assertEqual('', convert(0))
        self.assertEqual('1', convert(1))
        self.assertEqual('10', convert(2))
        self.assertEqual('1101', convert(13))
        self.assertEqual('1000101011', convert(555))


if __name__ == '__main__':
    unittest.main();
