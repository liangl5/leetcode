# Hint: median means both arrays will make up certain elements to the left and right of median. BS smaller array and calculate if valid split.
# First: note we do binary search to find the partition (so think of idx=2 includes the 2 values behind it, at idx 0 and 1)
# Next, we can calculate how many values we need from the other array, j, knowing the first partition index, i,
# and how many elements we need for one half of the median.
# If this is a correct split (l1 < r2 and l2 < r1), then we return either min(r1, r2) or (max(l1, l2) + min(r1, r2))/2
# If not a correct split and l1 > r2 (too many elements, so move r to i-1). And vice versa.

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        pass
