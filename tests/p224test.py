import unittest
from leetcode.p224 import Solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(2, Solution().calculate("1 + 1"))
        self.assertEqual(2, Solution().calculate("1+1"))

    def test_2(self):
        self.assertEqual(3, Solution().calculate(" 2-1 + 2 "))
        self.assertEqual(3, Solution().calculate(" 2-1 + 2"))
        self.assertEqual(3, Solution().calculate("2  -  1  +  2  "))
        self.assertEqual(3, Solution().calculate("2-1 + 2"))

    def test_3(self):
        self.assertEqual(23, Solution().calculate("(1+(4+5+2)-3)+(6+8)"))

    def test_4(self):
        self.assertEqual(2, Solution().calculate("1 - - 1"))
        self.assertEqual(0, Solution().calculate("1 + - 1"))
        self.assertEqual(-1, Solution().calculate("---1"))

    def test_5(self):
        self.assertEqual(-3, Solution().calculate("-(1+2)"))

    def test_6(self):
        self.assertEqual(123, Solution().calculate("123"))

    def test_7(self):
        self.assertEqual(12, Solution().calculate("(12)"))

    def test_41(self):
        self.assertEqual(-1, Solution().calculate("-2+ 1"))
        self.assertEqual(-3, Solution().calculate("-(2+ 1)"))
        self.assertEqual(-3, Solution().calculate("---(2+ 1)"))


if __name__ == '__main__':
    unittest.main()
