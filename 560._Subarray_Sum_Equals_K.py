from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        count = 0
        cache = {0: 1} 
        for num in nums:
            prefix_sum += num
            if prefix_sum - k in cache:
                count += cache[prefix_sum - k]
            cache[prefix_sum] = cache.get(prefix_sum, 0) + 1
        
        return count