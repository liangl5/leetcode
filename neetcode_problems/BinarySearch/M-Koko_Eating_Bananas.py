# Hint: O(nlogm), binary search 1 to maximum bananas
# Not sure if I would have gotten the solution easily if not given the recommended runtime of O(nlogm).
# The idea is to do a binary search from 1 to maximum bananas and then calculate how many hours it takes to get through the pile.
# Since we are doing binary search, any solution we get is guaranteed to be <= your current solution so no need for min.
from typing import List
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search between 1 and max(piles) to figure out optimal banana rate

        l, r = 1, max(piles)

        min_rate = r
        while l <= r:
            m = (l+r)//2
            #print("rate", m)

            hours = 0
            for b in piles:
                hours += math.ceil(b/m)
            #print(hours)

            if hours <= h:
                min_rate = m
                r = m-1
            else:
                l = m+1

        return min_rate
