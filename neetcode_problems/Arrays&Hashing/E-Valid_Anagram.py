# Hint: Counter or array with 26 spaces
# return Counter(s) == Counter(t). If you do this manually should use ord(c) - ord(‘a’) as this allows you to preallocate an array with length 26 and space is O(1)

from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)