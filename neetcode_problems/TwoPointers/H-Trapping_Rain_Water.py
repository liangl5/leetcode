# Hint: Track left and right max, move 2 pointers in.
# 2 pointer approach with some optimizations I missed.
# If we are moving left, then it will never be the case that left max > right max so we don't have to do min(l_max, r_max), just l_max is fine.
# Since we are setting l_max and r_max at the beginning, we do not need to check if l_max > height[l] to add area to the water,
# if they are equal then area += l_max - height[l] cancels out to 0 in the case that height[l] >= l_max.
# Can optimize my loop so that I set l_max = height[0] and r_max = height[-1] then begin looping the second element.
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        l_max = 0
        r_max = 0
        area = 0

        while l < r:
            l_max = max(l_max, height[l])
            r_max = max(r_max, height[r])
            #print(area, '\t', l, l_max, '\t', r, r_max)
            if height[l] < height[r]:

                area += l_max - height[l]
                l += 1
            else:

                area += r_max - height[r]
                r -= 1
            #print(area)
            #print('p2', area, '\t', l, l_max, '\t', r, r_max)
        return area