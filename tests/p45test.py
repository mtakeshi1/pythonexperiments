import unittest
from leetcode.p45 import Solution


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(2, Solution().jump([2, 3, 1, 1, 4]))

    def test_2(self):
        self.assertEqual(2, Solution().jump([2, 3, 0, 1, 4]))

    def test_3(self):
        self.assertEqual(0, Solution().jump([0]))

    def test_4(self):
        self.assertEqual(2, Solution().jump([1, 2, 3]))

    def test_5(self):
        self.assertEqual(3, Solution().jump([1, 1, 1, 1]))


if __name__ == '__main__':
    unittest.main()
