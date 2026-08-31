# Hint: DP right to left
# Stack method of adding descending values to stack, if you hit a non-descending value remove from the stack while you can
# The dynamic programming method is going right to left, if you add an element to the left,
# you find the max by following the right using previously calculated results.

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        pass
