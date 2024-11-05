from typing import List


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        total_skill = sum(skill)
        n = len(skill)
        
        if total_skill % (n // 2) != 0:
            return -1
        
        target_skill = total_skill // (n // 2)
        cache = {}
        result = 0
        for i in skill:
            if i in cache:
                cache[i] += 1
            else:
                cache[i] = 1
        for i in skill:
            if cache[i] > 0:
                diff = target_skill - i
                if diff in cache and cache[diff] > 0:
                    cache[i] -= 1
                    cache[diff] -= 1
                    if cache[i] < 0 or cache[diff] < 0:
                        return -1
                    result += i * diff
        if any(count > 0 for count in cache.values()):
            return -1
        
        return result