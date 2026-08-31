# Hint: update left and right of chains with max
# Was on the right track, c[num] = c[num-1] + c[num+1] + 1 but then needed to update the lowest in that chain
# and the greatest in that chain. Do this using c[num - c[num-1]] and c[num + c[num+1]].
# Instead of my solution of using a tuple of size 3.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        pass
