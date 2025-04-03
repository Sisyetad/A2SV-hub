# Problem: Median of Two Sorted Arrays - https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def merge(left, right):
            i = j = 0
            merged = []
            while i < len(left) and  j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            if i < len(left):
                merged.extend(left[i:])
            if j  < len(right):
                merged.extend(right[j:])
            return merged
        merged = merge(nums1, nums2)
        n = len(merged)
        if n % 2:
            return merged[n//2]
        else:
            left_median = merged[n//2 - 1]
            right_median = merged[n//2]
            return (left_median + right_median) / 2