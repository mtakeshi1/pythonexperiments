# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        acc = []
        queue = deque()
        queue.append(root)
        level_odd = False
        while len(queue) > 0:
            this_level_elements = len(queue)
            this_level = []
            for _ in range(this_level_elements):
                n = queue.popleft()
                this_level.append(n.val)
                if n.left is not None:
                    queue.append(n.left)
                if n.right is not None:
                    queue.append(n.right)
            if level_odd:
                this_level.reverse()
            acc.append(this_level)
            level_odd = not level_odd

        return acc
