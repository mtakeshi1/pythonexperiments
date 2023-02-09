import unittest
from leetcode.p438 import Solution


class SolTest(unittest.TestCase):
    def test1(self):
        sol = Solution()
        self.assertEqual([0, 6], sol.findAnagrams(s="cbaebabacd", p="abc"))

    def test2(self):
        sol = Solution()
        self.assertEqual([0, 1, 2], sol.findAnagrams(s="abab", p="ab"))


if __name__ == '__main__':
    unittest.main()
