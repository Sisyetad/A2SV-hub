# Problem: Count of Smaller Numbers After Self - https://leetcode.com/problems/count-of-smaller-numbers-after-self/

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n  
        indexed_nums = list(enumerate(nums))  
        def merge_sort(i, j, arr):
            if j - i == 1:
                return arr[i:j]

            mid = i + (j - i) // 2
            left = merge_sort(i, mid, arr)
            right = merge_sort(mid, j, arr)
            return merge(left, right)

        def merge(left, right):
            merged = []
            i = j = 0
            right_counter = 0  
            
            while i < len(left) and j < len(right):
                if left[i][1] <= right[j][1]:
                    result[left[i][0]] += right_counter  
                    merged.append(left[i])
                    i += 1
                else:
                    right_counter += 1
                    merged.append(right[j])
                    j += 1
            
            while i < len(left):
                result[left[i][0]] += right_counter
                merged.append(left[i])
                i += 1
            while j < len(right):
                merged.append(right[j])
                j += 1

            return merged

        merge_sort(0, n, indexed_nums)

        return result
