# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from AddTwoNumbers import ListNode


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_than_x = ListNode(0) 
        greater_than_x = ListNode(0) 
        less_pointer = less_than_x
        greater_pointer = greater_than_x

        while head:
            if head.val < x:
                less_pointer.next = head 
                less_pointer = less_pointer.next
            else:
                greater_pointer.next = head 
                greater_pointer = greater_pointer.next
            head = head.next

        greater_pointer.next = None 
        less_pointer.next = greater_than_x.next 

        return less_than_x.next  