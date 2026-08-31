# Hint: product can be split by front and back
# Division algorithm: keep track of how many 0's seen. > 1 = optimization, otherwise need logic to keep it out.
# Prefix & suffix: res[i] = nums[:i] * nums[i+1:] so 2 pass throughs that calculate half of the sum
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # double pass through solution
        # the sum of everything except nums[i] is nums[0:i] + nums[i+1:]
        # so can do 2 pass throughs
        res = [1] * len(nums)

        fw = bk = 1
        for i in range(len(nums)):
            res[i] *= fw
            fw *= nums[i]

            j = len(nums)-1-i
            res[j] *= bk
            bk *= nums[j]

        return res
