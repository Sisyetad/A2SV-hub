# Problem: Number of Pairs Satisfying Inequality - https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        arr = [a - b for a, b in zip(nums1, nums2)]
        result = 0

        def merge_sort(start, end):
            if start >= end:
                return [arr[start]]

            mid = (start + end) // 2
            left = merge_sort(start, mid)
            right = merge_sort(mid + 1, end)

            return merge(left, right)

        def merge(left, right):
            nonlocal result
            
            right_pnter = 0
            for left_val in left:
                while right_pnter < len(right) and left_val > right[right_pnter] + diff:
                    right_pnter += 1
                result += len(right) - right_pnter
                
            merged = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged

        merge_sort(0, len(arr) - 1)
        return result
