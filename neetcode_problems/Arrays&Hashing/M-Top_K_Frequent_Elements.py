# Hint: bucket sorting counts (white space is fine)
# Made a gnarly one liner using sort: return [x for x, _ in sorted(counts.items(), key=lambda x: x[1])][:k],
# one other solution (could be better) is using buckets (O(n) space) and iterate backwards returning the first k elements we find.

from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pass
