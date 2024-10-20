
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)  
        current = dummy  
        rem = 0
        while l1 or l2 or rem:
            firstValue = l1.val if l1 else 0 
            secondValue = l2.val if l2 else 0
            
            tempSum = firstValue + secondValue + rem
            rem = tempSum // 10 
            current.next = ListNode(tempSum % 10)  
            
            current = current.next 
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next
        