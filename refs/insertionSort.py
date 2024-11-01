# This is how Insertion Sort works:
# Insertion Sort builds the sorted list one item at a time by repeatedly inserting an element from the unsorted portion into its correct position in the sorted portion.

# Process:
# 1. Assume the first element is sorted.
# 2. Pick the next element in the unsorted portion.
# 3. Compare it backward with elements in the sorted portion and shift those that are larger by one position.
# 4. Insert the picked element in its correct position.
# 5. Repeat until all elements are sorted.

# Complexity:
# Worst-case time complexity: O(n^2)
# Best-case time complexity: O(n) when the list is already sorted.
# Space complexity: O(1) as it sorts in place.


from typing import List
#  [2 ,8, 5, 3, 9, 4]

from typing import List

def insertionSort(nums: List[int]) -> List[int]:
    for i in range(1, len(nums)):
        current = nums[i]
        j = i - 1
        # Shift elements of nums[0...i-1] that are greater than current
        while j >= 0 and nums[j] > current:
            nums[j + 1] = nums[j]
            j -= 1
        # Place the current element at its correct position
        nums[j + 1] = current
    return nums



print(insertionSort([2, 8, 5, 3, 9, 4])) # [2, 3, 4, 5, 8, 9]