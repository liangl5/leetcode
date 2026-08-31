# Hint: 2 Binary Searches
# My solution was 2 passthroughs, BS in all first values of each row, then BS the row.
# Best solution idea to to flatten 2d array into 1d then do basic BS (i.e. row, col = m//cols, m%cols)
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first do binary search on the row[0]
        # then can do binary search on the row itself

        r0, r1 = 0, len(matrix)-1

        while r0 <= r1:
            mid = (r0+r1)//2
            #print(l, mid, r)
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                r1 = mid-1
            else:
                r0 = mid+1

        l, r = 0, len(matrix[r1])-1

        while l <= r:
            mid = (l+r)//2
            if matrix[r1][mid] == target:
                return True
            elif matrix[r1][mid] > target:
                r = mid-1
            else:
                l = mid+1
        return False
            