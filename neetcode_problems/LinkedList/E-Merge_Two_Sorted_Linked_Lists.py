# Hint: 2 pointers
# Realized beginning check was not necessary since a dummy variable at the beginning would help make everything loop (cleaner code).
# Didn't know you could use an or between 2 variables and keep the variable (like l1 or l2 to check for uncaught values).

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        # guaranteed 1 in each.
        head = ListNode(val=-1)
        t = head
        while list1 and list2:
            #print('i')
            if list1.val < list2.val:
                t.next = list1
                list1 = list1.next
            else:
                t.next = list2
                list2 = list2.next
            
            t=t.next

        if list1:
            t.next = list1
        elif list2:
            t.next = list2

        return head.next
