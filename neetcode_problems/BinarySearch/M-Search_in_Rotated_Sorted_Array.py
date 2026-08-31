# Hint: BS but cases with rotation in one side
# Basically break it into cases where you figure out if the rotation is in the left or right,
# then you do corresponding checks to update l and r.
# Technically don't need a regular BS check but could offer some small optimization.
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums)-1

        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            #print(l, m, r)


            if nums[l] > nums[m]: # rotation is left
                #print("rotate is left")
                if target > nums[r] or target < nums[m]:
                    r = m-1
                else:
                    l = m+1

            else: # rotation is right
                #print("rotate is right")
                if target > nums[m] or target < nums[l]:
                    l = m+1
                    #print("good case")
                else:
                    r = m-1
        

        return -1
                    