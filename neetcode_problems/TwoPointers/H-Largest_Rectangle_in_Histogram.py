# Hint: similar to monotonic stack
# My approach was using a stack to basically keep / inherit all starting points for when you look at a new height.
# Ran into issues where I clear through the entire stack, the optimal solution only clears up to heights that are bigger than your current height,
# as now you keep track of the last one you cleared and this is the new starting index.

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        pass
