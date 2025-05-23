# Problem: Reverse Pairs - https://leetcode.com/problems/reverse-pairs/description/

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge(left, right):
            i = j = 0
            merged = []
            count = 0
            m, n = len(left), len(right)

            j_count = 0
            for i in range(m):
                while j_count < n and left[i] > 2 * right[j_count]:
                    j_count += 1
                count += j_count 

            i = j = 0
            while i < m and j < n:
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            while i < len(left):
                merged.append(left[i])
                i += 1
            while j < len(right):
                merged.append(right[j])
                j += 1
            return merged, count

        def merge_sort(i, j, arr):
            if j - i == 1:
                return arr[i:j], 0
            
            mid = i + (j - i) // 2
            left, left_count = merge_sort(i, mid, arr)
            right, right_count = merge_sort(mid, j, arr)

            merged, merge_count = merge(left, right)
            return merged, left_count + right_count + merge_count
        merged, ans = merge_sort(0, len(nums), nums)
        return ans