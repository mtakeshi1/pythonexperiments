import unittest
from leetcode.p1129 import Solution


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual([0, 1, -1], Solution().shortestAlternatingPaths(n=3, redEdges=[[0, 1], [1, 2]], blueEdges=[]))

    def test_2(self):
        self.assertEqual([0, 1, -1], Solution().shortestAlternatingPaths(n=3, redEdges=[[0, 1]], blueEdges=[[2, 1]]))

    def test_42(self):
        self.assertEqual([0, 2, -1, -1, 1],
                         Solution().shortestAlternatingPaths(n=5, redEdges=[[3, 2], [4, 1], [1, 4], [2, 4]],
                                                             blueEdges=[[2, 3], [0, 4], [4, 3], [4, 4], [4, 0],
                                                                        [1, 0]]))


if __name__ == '__main__':
    unittest.main()
