import unittest
from p32 import Solution


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(2, Solution().longestValidParentheses("(()"))

    def test_2(self):
        self.assertEqual(4, Solution().longestValidParentheses(")()())"))

    def test_3(self):
        self.assertEqual(0, Solution().longestValidParentheses(""))


if __name__ == '__main__':
    unittest.main()
