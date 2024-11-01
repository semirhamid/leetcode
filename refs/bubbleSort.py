# This is how Bubble Sort works:
# Bubble Sort repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. 
# This process repeats until no swaps are needed, meaning the list is sorted.

# Process:
# 1. Start from the beginning of the list.
# 2. Compare each pair of adjacent elements.
# 3. If the first element is greater than the second, swap them.
# 4. Continue this process, "bubbling" the largest element to the end of the list in each pass.
# 5. Repeat the passes over the list, each time ignoring the last sorted elements, until the list is sorted.

# Complexity:
# Worst-case time complexity: O(n^2)
# Best-case time complexity: O(n) if the list is already sorted.
# Space complexity: O(1) as it sorts in place.

# Code Example:
def bubble_sort(arr):
  n = len(arr)
  for i in range(n):
    swapped = False
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
        swapped = True
    if not swapped:
      break
  return arr
