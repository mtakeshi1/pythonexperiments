import unittest
from leetcode.p67 import Solution

class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual('100', Solution().addBinary('11', '1'))

    def test_2(self):
        self.assertEqual('10101', Solution().addBinary('1010', '1011'))


if __name__ == '__main__':
    unittest.main()
