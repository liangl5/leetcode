# Hint: BS but use M to figure out the rotation area
# My solution is to identify where the rotation is by comparing l, m, r.
# Since I am setting l=m or r=m, I have to end the loop early (while l < r-1) and this guarantees that r is the index of the min.
# The final case is when len <= 2 does not trigger the loop, return min of the edges.

class Solution:
    def findMin(self, nums: List[int]) -> int:
        pass
