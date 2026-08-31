# Hint: DP right to left
# Stack method of adding descending values to stack, if you hit a non-descending value remove from the stack while you can
# The dynamic programming method is going right to left, if you add an element to the left,
# you find the max by following the right using previously calculated results.
from typing import List
class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        res = [0] * len(temps)
        n = len(temps)
        stack = []


        for i in range(len(temps)-2, -1, -1):
            j = i + 1

            while j < n and temps[i] >= temps[j]:
                if res[j] == 0:
                    j = n
                    break
                else:
                    j += res[j]

            if j < n:
                res[i] = j - i

        return res
