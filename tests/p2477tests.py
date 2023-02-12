import unittest
from leetcode.p2477 import Solution


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(3, Solution().minimumFuelCost(roads=[[0, 1], [0, 2], [0, 3]], seats=5))

    def test_2(self):
        self.assertEqual(7, Solution().minimumFuelCost(roads=[[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6]], seats=2))

    def test_3(self):
        self.assertEqual(0, Solution().minimumFuelCost([], 1))


if __name__ == '__main__':
    unittest.main()
