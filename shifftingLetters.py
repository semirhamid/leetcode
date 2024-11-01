from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        numberRepresentation = [0 for c in s]
        numberRepresentation.append(0)
        for i , j , k in shifts[::-1]:
            numberRepresentation[i] += k
            numberRepresentation[j] -= k
            print(numberRepresentation)
        return
      


s = "abc"
shifts = [[0,1,0],[1,2,1],[0,2,1]]
sol = Solution()
print(sol.shiftingLetters(s, shifts)) # "bcd"