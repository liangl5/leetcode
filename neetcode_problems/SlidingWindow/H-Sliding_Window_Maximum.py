# Hint: Monotonic Stack / Queue
# The idea is you have a queue keeping the largest (and oldest values) on the left.
# Whenever you add a new value from the right you try to knock out as many values to the left as possible.
# Also make sure to check to see if the left is outdated.
# This ensures your maximum that is still in your window is to the left.

from collections import deque
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        res = []
        q = deque()

        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] <= nums[r]:
                q.pop()

            q.append(r)

            if l > q[0]:
                q.popleft()

            if r-l >= (k-1):
                res.append(nums[q[0]])
                l += 1
            r += 1

        return res
            
        