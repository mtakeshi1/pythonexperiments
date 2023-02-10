from typing import List


class Solution:

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    @staticmethod
    def calc_distance(grid, x, y, memo):
        cached = memo[x][y]
        if cached >= 0:
            return cached
        if grid[x][y] == 1:
            memo[x][y] = 0
            for direction in Solution.directions:
                nx = x + direction[0]
                ny = y + direction[1]
                if nx in range(0, len(grid)) and ny in range(0, len(grid)) and grid[nx][ny] != 1:
                    memo[nx][ny] = 1
            return 0

        distance = 1
        queue = [(x, y, 1)]
        while len(queue) > 0:
            xx, yy, distance = queue.pop(0)
            if grid[xx][yy] == 1:
                break
            for direction in Solution.directions:
                nx = xx + direction[0]
                ny = yy + direction[1]
                if nx in range(0, len(grid)) and ny in range(0, len(grid)):
                    queue.append((nx, ny, distance+1))
        #
        #         1
        memo[x][y] = distance
        return distance

    def maxDistance(self, grid: List[List[int]]) -> int:
        distances = [[-1 for _ in grid] for _ in grid]
        for i in range(len(grid)):
            for j in range(len(grid)):
                Solution.calc_distance(grid, i, j, distances)
        return max([max(x) for x in distances])
