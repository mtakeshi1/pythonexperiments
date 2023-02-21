import unittest
from leetcode.p540 import Solution


class MyTestCase(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(2, Solution().singleNonDuplicate([1, 1, 2]))
        self.assertEqual(1, Solution().singleNonDuplicate([1, 2, 2]))

    def test_1(self):
        self.assertEqual(2, Solution().singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))

    def test_2(self):
        self.assertEqual(10, Solution().singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]))  # add assertion here


if __name__ == '__main__':
    unittest.main()
