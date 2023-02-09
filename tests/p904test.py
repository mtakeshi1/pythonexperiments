import unittest
from leetcode.p904 import Solution


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(3, Solution().totalFruit([1, 2, 1]))

    def test_2(self):
        self.assertEqual(3, Solution().totalFruit([0, 1, 2, 2]))

    def test_3(self):
        self.assertEqual(4, Solution().totalFruit([1, 2, 3, 2, 2]))

    def test_4(self):
        self.assertEqual(5, Solution().totalFruit([1, 0, 1, 4, 1, 4, 1, 2, 3]))


if __name__ == '__main__':
    unittest.main()
