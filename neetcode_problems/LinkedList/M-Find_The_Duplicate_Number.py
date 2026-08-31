# Hint: the problem setup treats values an indices, allowing for cycle detection
# First didn't quite understand how the problem relate to linked lists, it makese sense now. 
# Cycle detection methodology only returns true or false if a cycle is detected, a second
# passthrough is required to find actual duplicate value (i.e. the start of the cycle). 
# Mathmatical formula is this: L (length of strip before cycle) + X (position in the cycle)
# Since fast & slow ended on same, then extra traveled distance (L+X) must equal some k*C(length of cycle)
# Now reset one of them, the other one is still on X. This means if you add L more steps, then both 
# pointers will have traveled to the start of the cycle (L+X) and (L) 

from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # basically do a cycle detection method
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
