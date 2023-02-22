from typing import List


class Solution:

    @staticmethod
    def min_days(weights: List[int], max_w: int) -> int:
        days = 0
        i = 0
        while i < len(weights):
            s = 0
            while i < len(weights) and s + weights[i] <= max_w :
                s += weights[i]
                i += 1
            if s == 0:
                return 999999
            days += 1
        return days


    def shipWithinDays(self, weights: List[int], days: int) -> int:
        min_w = 0
        max_w = sum(weights)
        while min_w < max_w:
            mid_w = min_w + (max_w - min_w) // 2
            d = Solution.min_days(weights, mid_w)
            if d == days:
                min_w = mid_w
                break
            elif d > days:
                min_w = mid_w + 1
            else:
                max_w = mid_w - 1
        while Solution.min_days(weights, min_w) <= days:
            min_w -= 1
        while Solution.min_days(weights, min_w) > days:
            min_w += 1
        return min_w

