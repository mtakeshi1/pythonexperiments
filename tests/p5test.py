import unittest
from leetcode.p5 import Solution


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual("bab", Solution().longestPalindrome("babad"))

    def test_2(self):
        self.assertEqual("bb", Solution().longestPalindrome("cbbd"))

    def test_single_char(self):
        self.assertEqual("a", Solution().longestPalindrome("a"))


if __name__ == '__main__':
    unittest.main()
