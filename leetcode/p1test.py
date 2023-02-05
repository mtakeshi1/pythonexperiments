import unittest
from p1 import Solution


class MyTestCase(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual([0, 1], s.twoSum(nums=[2, 7, 11, 15], target=9))  # add assertion here

    def test_2(self):
        s = Solution()
        self.assertEqual([1, 2], s.twoSum(nums=[3, 2, 4], target=6))  # add assertion here

    def test_3(self):
        s = Solution()
        self.assertEqual([0, 1], s.twoSum(nums=[3, 3], target=6))  # add assertion here


if __name__ == '__main__':
    unittest.main()
