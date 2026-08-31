# Hint: product can be split by front and back
# Division algorithm: keep track of how many 0's seen. > 1 = optimization, otherwise need logic to keep it out.
# Prefix & suffix: res[i] = nums[:i] * nums[i+1:] so 2 pass throughs that calculate half of the sum

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pass
