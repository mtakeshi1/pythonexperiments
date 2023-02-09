from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        half = len(nums)//2
        first, second = nums[:half], nums[half:]
        r = []
        for a, b in zip(first, second):
            r.append(a)
            r.append(b)
        return r