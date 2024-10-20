from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for index, element in enumerate(nums):
            diff = target - element
            if diff in hash:
                return [hash[diff], index]
            hash[element] = index