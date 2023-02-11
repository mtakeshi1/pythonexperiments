from typing import List


class Solution:
    def __init__(self):
        self.blue_edges = dict()
        self.red_edges = dict()
        self.distance_from_zero = dict()

    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        for f, to in blueEdges:
            self.blue_edges.setdefault(f, []).append(to)
        for f, to in redEdges:
            self.red_edges.setdefault(f, []).append(to)
        self.min_paths_from_zero()
        r = []
        for i in range(n):
            r.append(self.distance_from_zero.get(i, -1))
        return r

    def min_paths_from_zero(self):
        queue = [(0, 0, True), (0, 0, False)]
        visited_red = set()
        visited_blue = set()

        while len(queue) > 0:
            node, dist, blue = queue.pop(0)
            if node not in self.distance_from_zero or self.distance_from_zero[node] > dist:
                self.distance_from_zero[node] = dist
            if blue:
                if node in visited_blue:
                    continue
                else:
                    visited_blue.add(node)
                    for nd in self.red_edges.get(node, []):
                        queue.append((nd, dist + 1, False))
            if not blue:
                if node in visited_red:
                    continue
                else:
                    visited_red.add(node)
                    for nd in self.blue_edges.get(node, []):
                        queue.append((nd, dist + 1, True))
