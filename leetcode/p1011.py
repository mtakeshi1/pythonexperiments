from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        from math import ceil
        min_w = ceil(sum(weights) / days)
        i = 0
        for _ in range(days):
            s = 0
            while s < min_w and i < len(weights):
                s += weights[i]
                i += 1
            min_w = max(min_w, s)
        return min_w
