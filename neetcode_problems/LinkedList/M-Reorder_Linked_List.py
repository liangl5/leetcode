# Hint: divide into 2 sections
# My initial idea and algorithm was good, but the execution was a bit lacking.
# Basically find the midpoint, reverse the second half of the string, then can combine pretty easily.
# To find the midpoint without doing two passthroughs, we can use the fast and slow pointer until the fast hits the end.
# Reverse the string with basic logic. Then combine with basic logic

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2