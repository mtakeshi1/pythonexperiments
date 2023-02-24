from typing import List
from collections import OrderedDict
from sortedcontainers import SortedSet


class Solution:

    @staticmethod
    def deviation(nums: List[int]) -> int:
        return max(nums) - min(nums)

    def minimumDeviation(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        s = SortedSet(nums)
        changed = True
        r = max(s) - min(s)
        while changed:
            changed = False
            while min(s) % 2 == 1 and abs(min(s) * 2 < max(s)) < max(s) - min(s):
                a = s.pop(0)
                s.add(a * 2)
                changed = True
            while max(s) % 2 == 0 and abs(max(s) // 2 - min(s)) < max(s) - min(s):
                a = s.pop()
                s.add(a // 2)
                changed = True
            if max(s) - min(s) == r:
                break
            r = max(s) - min(s)
        return max(s) - min(s)
