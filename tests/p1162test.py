import unittest
from leetcode.p1162 import Solution


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(2, Solution().maxDistance([[1, 0, 1], [0, 0, 0], [1, 0, 1]]))

    def test_2(self):
        self.assertEqual(4, Solution().maxDistance([[1, 0, 0], [0, 0, 0], [0, 0, 0]]))


if __name__ == '__main__':
    unittest.main()
