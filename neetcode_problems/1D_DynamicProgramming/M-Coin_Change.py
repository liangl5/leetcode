# Hint: started from amount then DP backwards

# I like my solution because it is similar to BFS and keeping track of values that can be
# reached with # of coins used (the layers). Just need to make sure to keep track of 
# seen to not bloat the queue.

from typing import List
from collections import deque
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        queue = deque([amount])
        seen = set()
        coins_used = 0
        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                for j in coins:
                    if curr-j == 0:
                        return coins_used+1
                    elif curr-j > 0 and curr-j not in seen:
                        queue.append(curr-j)
                        seen.add(curr-j)

            #print(queue)
            coins_used += 1

        return -1

        
