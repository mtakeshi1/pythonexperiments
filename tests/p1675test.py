import unittest
from leetcode.p1675 import Solution


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(1, Solution().minimumDeviation([1, 2, 3, 4]))

    def test_2(self):
        self.assertEqual(3, Solution().minimumDeviation([4, 1, 5, 20, 3]))

    def test_3(self):
        self.assertEqual(1, Solution().minimumDeviation([3, 5]))

    def test_4(self):
        self.assertEqual(315, Solution().minimumDeviation([399, 908, 648, 357, 693, 502, 331, 649, 596, 698]))

    def test_dev1(self):
        self.assertEqual(3, Solution.deviation([4, 2, 5, 5, 3]))
        self.assertEqual(1, Solution.deviation([2, 2, 3, 2]))


if __name__ == '__main__':
    unittest.main()
