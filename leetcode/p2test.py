import unittest
from p2 import ListNode, Solution


class MyTestCase(unittest.TestCase):
    def test_1(self):
        l1 = ListNode.from_list([2, 4, 3])
        l2 = ListNode.from_list([5, 6, 4])
        expected = [7, 0, 8]
        self.assertEqual(expected, Solution().addTwoNumbers(l1, l2).to_list())  # add assertion here

    def test_5(self):
        l1 = ListNode.from_list([1, 1])
        l2 = ListNode.from_list([1, 1])
        expected = [2, 2]
        self.assertEqual(expected, Solution().addTwoNumbers(l1, l2).to_list())  # add assertion here


    def test_2(self):
        l1 = ListNode.from_list([0])
        l2 = ListNode.from_list([0])
        expected = [0]
        self.assertEqual(expected, Solution().addTwoNumbers(l1, l2).to_list())  # add assertion here

    def test_3(self):
        l1 = ListNode.from_list([9, 9, 9, 9, 9, 9, 9])
        l2 = ListNode.from_list([9, 9, 9, 9])
        expected = [8, 9, 9, 9, 0, 0, 0, 1]
        self.assertEqual(expected, Solution().addTwoNumbers(l1, l2).to_list())  # add assertion here


if __name__ == '__main__':
    unittest.main()
