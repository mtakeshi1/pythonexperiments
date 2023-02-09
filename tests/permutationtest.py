import unittest
import permutation


class SolTest(unittest.TestCase):
    def test1(self):
        sol = permutation.Solution()
        self.assertEqual(True, sol.checkInclusion("", ""))

    def test2(self):
        sol = permutation.Solution()
        self.assertEqual(True, sol.checkInclusion("ab", "eidbaooo"))

    def test3(self):
        sol = permutation.Solution()
        self.assertEqual(False, sol.checkInclusion(s1="ab", s2="eidboaoo"))
