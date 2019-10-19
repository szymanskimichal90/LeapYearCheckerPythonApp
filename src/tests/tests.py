import unittest
from src.main import checkIfYearIsLeap


class MyTestCase(unittest.TestCase):
    def test_isYear2004Leap(self):
        data = "Year is leap"
        result = checkIfYearIsLeap(2004)
        self.assertEqual(data, result)

    def test_isYear2005Leap(self):
        data = "Year is not leap"
        result = checkIfYearIsLeap(2005)
        self.assertEqual(data, result)

    def test_isYear2100Leap(self):
        data = "Year is not leap"
        result = checkIfYearIsLeap(2100)
        self.assertEqual(data, result)

    def test_isYear2000Leap(self):
        data = "Year is leap"
        result = checkIfYearIsLeap(2000)
        self.assertEqual(data, result)


if __name__ == '__main__':
    unittest.main()
