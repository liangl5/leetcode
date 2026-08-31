# Hint: update left and right of chains with max
# Was on the right track, c[num] = c[num-1] + c[num+1] + 1 but then needed to update the lowest in that chain
# and the greatest in that chain. Do this using c[num - c[num-1]] and c[num + c[num+1]].
# Instead of my solution of using a tuple of size 3.
from collections import defaultdict
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        res = 0

        for num in nums:
            if not mp[num]:
                mp[num] = mp[num - 1] + mp[num + 1] + 1
                mp[num - mp[num - 1]] = mp[num]
                mp[num + mp[num + 1]] = mp[num]
                res = max(res, mp[num])
        return res
