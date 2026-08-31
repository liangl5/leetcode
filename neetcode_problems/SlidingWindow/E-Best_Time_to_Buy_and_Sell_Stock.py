# Hint: 1 passthrough, keeping local min
# Thought of it as 1 passthrough, keeping a local min on the leftside,
# checking to see if our profit increases if we introduce a new element (new - local min).
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP