# Hint: track cooldowns with a queue and max heap to get the next task with the most remaining count.

# task actually doesnt matter, track the value. 
# queue for cooldowns is necessary

from collections import deque, Counter
import heapq
from typing import List
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [-cnt for cnt in count.values()]

        heapq.heapify(heap)
        #print(heap)


        cooldown = deque() # -cnt, idletime

        time = 0
        while heap or cooldown:
            time += 1

            if not heap:
                time = cooldown[0][1]
            else:
                cnt = 1 + heapq.heappop(heap)
                if cnt:
                    cooldown.append((cnt, time+n))

            if cooldown and cooldown[0][1] == time:
                heapq.heappush(heap, cooldown.popleft()[0])

        return time