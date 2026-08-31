# Hint: BS but use M to figure out the rotation area
# My solution is to identify where the rotation is by comparing l, m, r.
# Since I am setting l=m or r=m, I have to end the loop early (while l < r-1) and this guarantees that r is the index of the min.
# The final case is when len <= 2 does not trigger the loop, return min of the edges.
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]