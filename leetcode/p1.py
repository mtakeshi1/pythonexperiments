from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = dict()
        for i, num in enumerate(nums):
            remaining = target - num
            if visited.get(remaining) is not None:
                return [visited[remaining], i]
            else:
                visited[num] = i
        return []

