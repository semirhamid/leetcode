from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = 0
        while right < len(nums):
            if nums[right] != 0:
                # Swap only if `right` points to a non-zero element
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            # Move the `right` pointer to continue scanning
            right += 1
