# Hint: (carry logic with linked lists)

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        new = ListNode(0)
        new_it = new

        l1_it = l1
        l2_it = l2

        carry = 0
        while l1_it and l2_it:
            new_it.next = ListNode((l1_it.val + l2_it.val + carry)%10)
            carry = (l1_it.val + l2_it.val + carry) // 10

            l1_it = l1_it.next
            l2_it = l2_it.next
            new_it = new_it.next

        # after calculating the shared digits, check for remaining and also carry
        if l1_it or l2_it:
            it = l1_it if l1_it else l2_it
            while it:
                new_it.next = ListNode((it.val+carry)%10)
                carry = (it.val+carry) // 10

                it = it.next
                new_it = new_it.next

        if carry:
            new_it.next = ListNode(carry)


        return new.next
