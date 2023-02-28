# Definition for a binary tree node.
from typing import Optional, List
from collections import Counter


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.trees = Counter()
        self.results = set()

    def traverse(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return '-'
        left_child = self.traverse(root.left)
        r = self.traverse(root.right)
        # figure out why pre-order traversal give the correct result, but in-order traversal doesn't
        # formatted = left_child + '|' + str(root.val) + '|' + r
        formatted = str(root.val) + '|' + left_child + '|' + r

        if self.trees.get(formatted) == 1:
            self.results.add(root)
        self.trees[formatted] += 1
        return formatted

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.traverse(root)
        return list(self.results)


if __name__ == '__main__':
    tree = TreeNode(0,
                    left=TreeNode(0, left=TreeNode(0)),
                    right=TreeNode(0, right=TreeNode(0, right=TreeNode(0)))
                    )
    ll = Solution().findDuplicateSubtrees(tree)
    print([c.val for c in ll])
