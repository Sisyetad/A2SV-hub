# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(left_half, right_half):
            merged = []
            left, right = 0, 0
            while left < len(left_half) and right < len(right_half):
                if left_half[left] <= right_half[right]:
                    merged.append(left_half[left])
                    left += 1
                else:
                    merged.append(right_half[right])
                    right += 1
            if left < len(left_half):
                merged.extend(left_half[left:])
            if right < len(right_half):
                merged.extend(right_half[right:])
            return merged
        def mergeSort(arr, start, end):
            if end - start == 1:
                return arr[start:end]

            mid = (end + start) // 2
            left_half = mergeSort(arr, start, mid)
            right_half = mergeSort(arr, mid, end)
            return merge(left_half, right_half)
        return mergeSort(nums, 0, len(nums))