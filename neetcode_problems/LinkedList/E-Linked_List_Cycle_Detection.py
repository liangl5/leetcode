# Hint: fast and slow pointer
# Easy solution of having a fast pointer (increments by 2 steps each time) and a slow pointer (increments by 1 step each time).
# If they equal each other at a certain point that means that there must be a cycle. If we reach the end then no cycle.
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head.next
        slow = head

        while fast and fast.next:
            if fast == slow:
                return True

            fast = fast.next.next
            slow = slow.next

        return False
