# Hint: array with 26 spaces
# Idea: hash all anagrams to one value, use defaultdict(list). Initially tried Counter but Counter is unhashable.
# Used the ord(c) - ord('a') trick to preallocate an array of 26, have to cast as tuple() then we can return list(hash_map.values())

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pass
