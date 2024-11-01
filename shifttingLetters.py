from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        shift_accum = [0] * (len(s) + 1)
        for start, end, direction in shifts:
            delta = 1 if direction == 1 else -1
            shift_accum[start] += delta
            shift_accum[end + 1] -= delta

        cumulative_shift = 0
        result = []
        for i in range(len(s)):
            cumulative_shift += shift_accum[i]
            shifted_char = chr((ord(s[i]) - ord('a') + cumulative_shift) % 26 + ord('a'))
            result.append(shifted_char)

        return ''.join(result)


sol = Solution()
print(sol.shiftingLetters("abc", [[0, 1, 0], [1, 2, 1]]))  # Example output
