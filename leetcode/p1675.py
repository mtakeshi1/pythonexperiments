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
        s = SortedSet([n * 2 if n % 2 == 1 else n for n in nums])
        min_f = max(s) - min(s)
        while s[-1] % 2 == 0:
            v = s.pop() // 2
            s.add(v)
            min_f = min(min_f, s[-1] - s[0])
        return min_f


