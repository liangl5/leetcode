# Hint: Dynamic Size Sliding Window
# My solution: have a char set that keeps track of all the chars you have seen.
# If you come across a char you have seen, then move l up until you hit the char (forgot to remove the chars from the set).
# Optimal solution: use a dictionary to keep a char and occurrence. If you have already seen the char, move l=max(seen[s[r]], l).

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pass
