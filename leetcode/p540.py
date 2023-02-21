from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)

        ans = -1
        while ans < 0:
            mid = low + (high - low) // 2
            left_has = mid > 0 and nums[mid - 1] == nums[mid]
            right_has = mid < len(nums) - 1 and nums[mid + 1] == nums[mid]
            if not left_has and not right_has:
                ans = mid
                break
            left = mid
            if left_has:
                left = mid - 1
            if left % 2 == 0:
                low = mid + 1
            else:
                high = mid - 1

        return nums[ans]
        # [1 1 2 2 3]
        # [1 2 2 3 3]
        # [1 1 2 2 3 4 4 5 5]
        # [1 1 2 3 3 4 4 5 5]
        # [1 1 2 2 3 3 4 5 5]