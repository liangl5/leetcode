# Hint: Hashmap & complement
# Smart usage of enumerate and sorted(key=..). The best way is to loop through, keeping track of complement and index.
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}

        for i, num in enumerate(nums):
            if num in res:
                return [res[num], i]
            
            res[target-num] = i