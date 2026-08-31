# Hint: similar to monotonic stack
# My approach was using a stack to basically keep / inherit all starting points for when you look at a new height.
# Ran into issues where I clear through the entire stack, the optimal solution only clears up to heights that are bigger than your current height,
# as now you keep track of the last one you cleared and this is the new starting index.
from typing import List
from collections import deque

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = heights[0]
        min_heap = deque([(heights[0], 0)])

        for i in range(1, len(heights)):
            #print(area, min_heap, i)

            area = max(area, heights[i])
            seen_min_heights = {heights[i]: i}
            for _ in range(len(min_heap)):
                h, idx = min_heap.pop()
                
                min_height = min(h, heights[i])

                #print(h, idx, min_height * (i-idx+1))
                area = max(area, min_height * (i-idx+1))

                if min_height in seen_min_heights:
                    seen_min_heights[min_height] = min(seen_min_heights[min_height], idx)
                else:
                    seen_min_heights[min_height] = idx

            #print(seen_min_heights)
            for key, val in seen_min_heights.items():
                min_heap.append((key, val))
            #print(area, min_heap, seen_min_heights, i)


        return area