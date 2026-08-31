# Hint: two passthrough, using a mapping to track unique nodes
# My thought process was correct but for some reason was thinking of using an array to keep track of positioning and finds
# instead of just doing a mapping with nodes as the keys.

from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # first passthrough to copy all nodes and track mappings
        old_it = head
        new = Node(0)
        new_it = new
        mapping = {}

        while old_it:
            new_it.next = Node(old_it.val)
            mapping[old_it] = new_it.next
            new_it = new_it.next
            old_it = old_it.next

        # final passthrough
        new = new.next
        
        old_it = head
        new_it = new

        while old_it:
            if old_it.random:
                #print(old_it.random.val)
                new_it.random = mapping[old_it.random]
            old_it = old_it.next
            new_it = new_it.next

        return new