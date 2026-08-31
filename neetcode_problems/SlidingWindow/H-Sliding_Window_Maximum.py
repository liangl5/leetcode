# Hint: Monotonic Stack / Queue
# The idea is you have a queue keeping the largest (and oldest values) on the left.
# Whenever you add a new value from the right you try to knock out as many values to the left as possible.
# Also make sure to check to see if the left is outdated.
# This ensures your maximum that is still in your window is to the left.

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        pass
