import unittest
from leetcode.p1011 import Solution


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(15, Solution().shipWithinDays(weights=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], days=5))

    def test_2(self):
        self.assertEqual(6, Solution().shipWithinDays(weights=[3, 2, 2, 4, 1, 4], days=3))

    def test_3(self):
        self.assertEqual(3, Solution().shipWithinDays(weights=[1, 2, 3, 1, 1], days=4))


if __name__ == '__main__':
    unittest.main()
