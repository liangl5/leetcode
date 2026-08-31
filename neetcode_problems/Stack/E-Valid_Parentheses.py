# Hint: stack & mapping
# Basic stack usage, checking to see if stack is empty, adding, or popped matches.
from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        mapping = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in mapping.values():
                stack.append(c)
            elif c in mapping:
                if not stack or stack.pop() != mapping[c]:
                    return False
        
        return len(stack) == 0