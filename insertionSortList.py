from typing import Optional

from AddTwoNumbers import ListNode


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        current = head.next
        head.next = None

        while current:
            next_node = current.next
            pos = dummy
            while pos.next and pos.next.val < current.val:
                pos = pos.next

            current.next = pos.next
            pos.next = current
            current = next_node

        return dummy.next