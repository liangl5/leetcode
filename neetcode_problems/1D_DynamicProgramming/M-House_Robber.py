# Hint: Building left to right, can always track maximum solution
# padding is not necessary but allows me to do a basic loop without worrying about
# an array with only size of 1 or 2

from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        nums = [0] + nums # add left pading for elegant solution
        for i in range(2, len(nums)):
            nums[i] = max(nums[i-1], nums[i-2] + nums[i])

        return nums[-1]

