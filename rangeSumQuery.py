from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = [nums[0]]
        for i in range(1, len(nums)):
            self.nums.append(self.nums[i - 1] + nums[i])  # Cumulative sum up to i

    def sumRange(self, left: int, right: int) -> int:
        left_sum = 0 if left == 0 else self.nums[left - 1]
        right_sum = self.nums[right]
        return right_sum - left_sum