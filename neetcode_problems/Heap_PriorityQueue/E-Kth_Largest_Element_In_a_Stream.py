# Hint: largest means only need to keep track of k elements (can pop the rest)

# need the final pop and boolean checkfor an edge case of empty and adding 1 element to it. 
# if you wanted the k smallest it would be the same but with a max heap instead of a min heap

from typing import List
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        heapq.heapify(self.nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]
