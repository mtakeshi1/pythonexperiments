from typing import List


class Solution:

    @staticmethod
    def min_jumps(nums, from_index, memo):
        if from_index >= len(nums)-1:
            return 0
        if from_index in memo:
            return memo[from_index]
        max_jump = nums[from_index]
        best = len(nums)
        for j in range(from_index + 1, from_index + 1 + max_jump):
            best = min(best, Solution.min_jumps(nums, j, memo) + 1)
        memo[from_index] = best
        return best

    @staticmethod
    def min_jumps_fast(nums):
        jumps = 0
        cur_end = 0
        cur_far = 0
        for i in range(len(nums) - 1):
            cur_far = max(cur_far, i + nums[i])

            if i == cur_end: # last known position
                jumps += 1
                cur_end = cur_far
        return jumps

    def jump(self, nums: List[int]) -> int:
        # return Solution.min_jumps(nums, 0, dict())
        return Solution.min_jumps_fast(nums)


