# Hint: 3 pointers, 1 is negative, other 2 pointers do two-sum
# Use 3 pointers, one that goes through all negatives and zeros (if we hit a positive, only positives are left and cannot equal 0),
# 2 that are used for 2Sum. Making sure to skip duplicates on one side when we hit a triplet.
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0
        while i < len(nums)-2:
            # this means we only have positive number left, cannot get to 0
            if nums[i] > 0:
                break

            # skips the duplicated v
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue


            l, r = i+1, len(nums)-1

            while l < r:
                t = nums[i] + nums[l] + nums[r]
                if t == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    # skip
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

                elif t < 0:
                    l += 1
                elif t > 0:
                    r -= 1

            i += 1

        return res


