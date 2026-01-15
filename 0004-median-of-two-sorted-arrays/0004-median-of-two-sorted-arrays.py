class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums_joined = nums1 + nums2
        list.sort(nums_joined)
        size_sorted = len(nums_joined)
        mid = size_sorted // 2
        if size_sorted % 2 == 0:
            return (nums_joined[mid] + nums_joined[mid-1])/2
        elif size_sorted % 2 == 1:
            return nums_joined[mid]

        