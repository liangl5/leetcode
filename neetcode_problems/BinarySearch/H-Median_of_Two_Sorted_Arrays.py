# Hint: median means both arrays will make up certain elements to the left and right of median. BS smaller array and calculate if valid split.
# First: note we do binary search to find the partition (so think of idx=2 includes the 2 values behind it, at idx 0 and 1)
# Next, we can calculate how many values we need from the other array, j, knowing the first partition index, i,
# and how many elements we need for one half of the median.
# If this is a correct split (l1 < r2 and l2 < r1), then we return either min(r1, r2) or (max(l1, l2) + min(r1, r2))/2
# If not a correct split and l1 > r2 (too many elements, so move r to i-1). And vice versa.
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        # nums1 guaranteed smaller
        n, m = len(nums1), len(nums2)
        l, r = 0, n
        total = n+m
        half = total // 2

        while l <= r:
            i = (l+r)//2 # partition in nums1
            j = half - i # partition in nums2
            
            l1 = nums1[i-1] if i > 0 else float('-inf')
            r1 = nums1[i] if i < n else float('inf')
            l2 = nums2[j-1] if j > 0 else float('-inf')
            r2 = nums2[j] if j < m else float('inf')

            # so valid
            if l1 <= r2 and l2 <= r1:
                if total % 2 == 1: # odd
                    return min(r1, r2)
                else:
                    return (max(l1, l2) + min(r1, r2))/2

            elif l1 > r2:
                r = i-1
            else:
                l = i+1
            
