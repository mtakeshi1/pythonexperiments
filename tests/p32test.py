import unittest
import p32


class MyTestCase(unittest.TestCase):
    def test_1(self):
        s = p32.Solution()
        self.assertEqual(2, s.longestValidParentheses("(()"))  # add assertion here

    def test_2(self):
        s = p32.Solution()
        self.assertEqual(4, s.longestValidParentheses(")()())"))  # add assertion here

    def test_3(self):
        s = p32.Solution()
        self.assertEqual(2, s.longestValidParentheses("))))()"))  # add assertion here

    def test_4(self):
        s = p32.Solution()
        self.assertEqual(4, s.longestValidParentheses("(())"))  # add assertion here

    def test_empty(self):
        s = p32.Solution()
        self.assertEqual(0, s.longestValidParentheses(""))  # add assertion here


if __name__ == '__main__':
    unittest.main()
