# Hint: Traverse but lots of pointers needed and order of operations matter
# The easiest way to not get dizzy is to draw a diagram with order of operations and 
# have descriptive variable names.

from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        start = ListNode(val=0, next=head)

        l1 = start
        it = start

        seen = 0
        while it.next:
            it = it.next
            seen += 1

            if seen == k:
                seen = 0

                curr = l1.next
                new_l1 = curr
                l1.next = it # new left connection to reversed part
                
                r2 = it.next
                prev = r2 # new right connection to reversed part

                # basic code to reverse a section
                for i in range(k):
                    next = curr.next
                    curr.next = prev

                    curr, prev = next, curr

                # reset the two pointers used to keep track of left (l1) and iterator (it)
                l1 = new_l1
                it=l1

        
        return start.next