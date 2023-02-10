import unittest
from leetcode.p1162 import Solution


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(2, Solution().maxDistance2([[1, 0, 1], [0, 0, 0], [1, 0, 1]]))

    def test_2(self):
        self.assertEqual(4, Solution().maxDistance2([[1, 0, 0], [0, 0, 0], [0, 0, 0]]))

    def test_3(self):
        self.assertEqual(-1, Solution().maxDistance2([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))

    def test_4(self):
        self.assertEqual(-1, Solution().maxDistance2([[1, 1, 1], [1, 1, 1], [1, 1, 1]]))

    def test_5(self):
        self.assertEqual(2, Solution().maxDistance2(
            [[1, 0, 0, 0, 0, 1, 0, 0, 0, 1], [1, 1, 0, 1, 1, 1, 0, 1, 1, 0], [0, 1, 1, 0, 1, 0, 0, 1, 0, 0],
             [1, 0, 1, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
             [0, 0, 0, 1, 1, 1, 1, 0, 0, 1], [0, 1, 0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
             [1, 1, 0, 1, 1, 1, 1, 1, 0, 0]]))


#
if __name__ == '__main__':
    unittest.main()
