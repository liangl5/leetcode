# Hint: Sliding Window w/ Maximum Frequency
# My solution didn't work, it would have also been O(m*n) as for every character I go ahead and update all the distinct characters,
# trying to make the logic work.
# Optimal solution: think of a sliding window where you keep track of the maximum frequency of a single character in your sliding window.
# This means you can calculate how many k is required to make our sliding window valid. If it is too much, then I have to remove it from the left.
# Very efficient as once something makes your window invalid, you just shift your window to the right (same size).
# (Think if you have a window size of 4, adding 1 more breaks it, so you just shift right until you find a group of 5 characters that work together, since we want max.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        pass
