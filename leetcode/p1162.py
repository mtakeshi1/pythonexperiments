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

        distance = 0
        queue = [(x, y, 0)]
        visited = set()
        while len(queue) > 0:
            xx, yy, distance = queue.pop(0)
            if grid[xx][yy] == 1:
                break
            if memo[xx][yy] != -1:
                distance = distance + memo[xx][yy]
                break
            if (xx, yy) in visited:
                continue
            visited.add((xx, yy))
            for direction in Solution.directions:
                nx = xx + direction[0]
                ny = yy + direction[1]
                if nx in range(0, len(grid)) and ny in range(0, len(grid)):
                    queue.append((nx, ny, distance+1))
        if len(queue) == 0:
            return -1

        memo[x][y] = distance
        return distance

    def maxDistance2(self, grid: List[List[int]]) -> int:
        distances = [[-1 for _ in grid] for _ in grid]
        queue = []
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == 1:
                    queue.append((i, j))
        if len(queue) == 0 or len(queue) == len(grid) * len(grid):
            return -1

        dist = 0
        while len(queue) > 0:
            next_queue = []
            while len(queue) > 0:
                x, y = queue.pop()
                if distances[x][y] != -1:
                    continue
                distances[x][y] = dist
                for direction in Solution.directions:
                    nx = x + direction[0]
                    ny = y + direction[1]
                    if nx in range(0, len(grid)) and ny in range(0, len(grid)) and distances[nx][ny] == -1:
                        next_queue.append((nx, ny))
            queue = next_queue
            dist += 1
        return max([max(x) for x in distances])

    def maxDistance(self, grid: List[List[int]]) -> int:
        distances = [[-1 for _ in grid] for _ in grid]
        for i in range(len(grid)):
            for j in range(len(grid)):
                Solution.calc_distance(grid, i, j, distances)
        r = max([max(x) for x in distances])
        if r == 0:
            return -1
        return r
