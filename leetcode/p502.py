from collections import deque
from typing import List
import heapq

class Solution:

    def findMaximizedCapitalGreedy(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        money = w
        reqs = []
        profs = []
        for i in range(len(profits)):
            if capital[i] <= money:
                heapq.heappush(profs, -profits[i])
            else:
                heapq.heappush(reqs, (capital[i], i))

        for _ in range(k):
            if len(profs) == 0:
                break
            best = heapq.heappop(profs)
            money += -best
            while len(reqs) > 0 and reqs[0][0] <= money:
                i = heapq.heappop(reqs)[1]
                heapq.heappush(profs, -profits[i])
        return money

    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        previous = [w for _ in range(len(profits))]
        # need to keep track of what was used
        used = set()
        for _ in range(min(k, len(profits))):
            current = previous.copy()
            selected = -1
            for i in range(len(profits)):
                if i in used:
                    continue
                if previous[i] >= capital[i]:
                    if i == 0 or (i > 0 and previous[i] + profits[i] > current[i-1]):
                        selected = i
                        current[i] = previous[i] + profits[i]
                    else:
                        current[i] = current[i-1]
                elif i > 0:
                    current[i] = current[i - 1]
            previous = current
            if selected == -1:
                break
            used.add(selected)
        return previous[-1]

    def findMaximizedCapital_1(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        max_found = 0
        queue = deque()
        for i in range(len(profits)):
            if capital[i] <= w:
                queue.append((w + profits[i], {i}))

        while len(queue) > 0:
            money, visited = queue.popleft()
            max_found = max(max_found, money)
            if len(visited) == k or len(visited) == len(profits):
                max_found = max(max_found, money)
            else:
                for i in range(len(profits)):
                    if i not in visited and capital[i] <= money:
                        visited2 = visited.copy()
                        visited2.add(i)
                        queue.append((money + profits[i], visited2))
        return max_found
