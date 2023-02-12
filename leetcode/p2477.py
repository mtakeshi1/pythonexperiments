from typing import List


class Solution:

    @staticmethod
    def count_fuel(tree, subtrees, seats, node):
        from math import ceil
        fuel = 0
        for child in tree.get(node, set()):
            fuel += ceil((1 + subtrees.get(child, 0)) / seats)
            fuel += Solution.count_fuel(tree, subtrees, seats, child)
        return fuel

    @staticmethod
    def count_subtress(tree, subtrees, node):
        if node in subtrees:
            return subtrees[node]
        sub = 0
        for child in tree.get(node, set()):
            sub += 1 + Solution.count_subtress(tree, subtrees, child)
        subtrees[node] = sub
        return sub

    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        connections = dict()
        for f, t in roads:
            connections.setdefault(f, set()).add(t)
            connections.setdefault(t, set()).add(f)
        tree = dict()
        visited = set()
        from collections import deque
        queue = deque()
        queue.append(0)
        while len(queue) > 0:
            n = queue.popleft()
            if n in visited:
                continue
            visited.add(n)
            for conn in connections.get(n, set()):
                if conn not in visited:
                    tree.setdefault(n, []).append(conn)
                    queue.append(conn)
        subtrees = dict()
        Solution.count_subtress(tree, subtrees, 0)
        return Solution.count_fuel(tree, subtrees, seats, 0)
