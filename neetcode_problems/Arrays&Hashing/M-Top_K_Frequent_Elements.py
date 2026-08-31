# Hint: bucket sorting counts (white space is fine)
# Made a gnarly one liner using sort: return [x for x, _ in sorted(counts.items(), key=lambda x: x[1])][:k],
# one other solution (could be better) is using buckets (O(n) space) and iterate backwards returning the first k elements we find.

from collections import defaultdict
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        freq = [[] for i in range(len(nums)+1)]
        for num in nums:
            counts[num] += 1

        for num, cnt in counts.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res