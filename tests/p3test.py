import unittest
from leetcode.p3 import Solution


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(3, Solution().lengthOfLongestSubstring("abcabcbb"))

    def test_2(self):
        self.assertEqual(1, Solution().lengthOfLongestSubstring("bbbbb"))

    def test_3(self):
        self.assertEqual(3, Solution().lengthOfLongestSubstring("pwwkew"))

    def test_4(self):
        self.assertEqual(1, Solution().lengthOfLongestSubstring("a"))

if __name__ == '__main__':
    unittest.main()
