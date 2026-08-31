# Hint: delayed pointer w/ dummy
# My implementation felt off by one for a majority of it as I didn't properly calculate the number of steps.
# Basically the far right pointer should be ahead by n steps as this allows us to know which node to cut.
# The dummy variable at beginning allows us to remove the head more easily.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(val=None, next=head)

        fast = head
        while n > 0:
            fast = fast.next
            n -= 1

        s = dummy
        while fast:
            fast = fast.next
            s = s.next

        #print(s.val)
        s.next = s.next.next

        return dummy.next
        #print(s.val)