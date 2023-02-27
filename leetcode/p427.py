from typing import List


# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


def all_ones(grid: List[List[int]], min_row, max_row, min_col, max_col):
    for row in grid[min_row:max_row]:
        for v in row[min_col:max_col]:
            if v == 0 or not v:
                return False
    return True


def all_zeros(grid: List[List[int]], min_row, max_row, min_col, max_col):
    for row in grid[min_row:max_row]:
        for v in row[min_col:max_col]:
            if v == 1 or v:
                return False
    return True


def build_rec(grid: List[List[int]], min_row, max_row, min_col, max_col):
    if max_row == min_row + 1 and max_col == min_col + 1:
        return Node(grid[min_row][min_col] == 1, True, None, None, None, None)

    if all_ones(grid, min_row, max_row, min_col, max_col):
        return Node(True, True, None, None, None, None)

    if all_zeros(grid, min_row, max_row, min_col, max_col):
        return Node(False, True, None, None, None, None)

    mid_row = (min_row + max_row) // 2
    mid_col = (min_col + max_col) // 2
    top_left = build_rec(grid, min_row, mid_row, min_col, mid_col)
    top_right = build_rec(grid, min_row, mid_row, mid_col, max_col)
    bot_left = build_rec(grid, mid_row, max_row, min_col, mid_col)
    bot_right = build_rec(grid, mid_row, max_row, mid_col, max_col)
    return Node(False, False, top_left, top_right, bot_left, bot_right)


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        return build_rec(grid, 0, len(grid), 0, len(grid))


if __name__ == '__main__':
    n = Solution().construct(
        [[1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0]])
    print(n)
