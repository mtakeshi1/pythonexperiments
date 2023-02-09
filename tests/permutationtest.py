import unittest
from leetcode.permutation import *


class SolTest(unittest.TestCase):
    def test1(self):
        sol = Solution()
        self.assertEqual(True, sol.checkInclusion("", ""))

    def test2(self):
        sol = Solution()
        self.assertEqual(True, sol.checkInclusion("ab", "eidbaooo"))

    def test3(self):
        sol = Solution()
        self.assertEqual(False, sol.checkInclusion(s1="ab", s2="eidboaoo"))
