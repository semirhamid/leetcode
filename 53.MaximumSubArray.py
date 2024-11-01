from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx_sum = float('-inf')
        curr_sum = 0
        for num in nums:
            curr_sum = max(num, curr_sum + num)
            mx_sum = max(mx_sum, curr_sum)
        return mx_sum

        