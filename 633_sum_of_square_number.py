from cmath import sqrt


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(sqrt(c))
        while left <= right:
            result = left * left + right * right
            if result == c:
                return True
            elif result < c:
                left += 1
            else:
                right -= 1
        return False
