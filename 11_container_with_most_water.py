from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        mx = 0
        while left < right:
            width = right - left
            vertical = min(height[left], height[right])
            current_content = width * vertical
            mx = max(mx , current_content)
            if height[right] < height[left]:
                right -= 1
            else:
                left += 1
        return mx