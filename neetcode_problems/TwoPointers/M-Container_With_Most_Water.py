# Hint: 2 pointer, keep highest barrier
# Basic left and right pointer, keep the highest barrier and move the lowest barrier.
from typing import List
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        res = 0
        while l < r:
            #print(l, r, min(heights[l], heights[r]) * (r-l))
            res = max(res, min(heights[l], heights[r]) * (r-l))

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return res

