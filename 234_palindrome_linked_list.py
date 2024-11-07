# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from AddTwoNumbers import ListNode


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        box = []
        while head:
            box.append(head.val)
            head = head.next
        return box == box[::-1]
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True  # A list with 0 or 1 node is always a palindrome

        # Step 1: Find the middle of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the linked list
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        # Step 3: Compare the first half with the reversed second half
        left, right = head, prev
        while right:  # Only need to compare until the end of the right half
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        # If all nodes matched, it is a palindrome
        return True
