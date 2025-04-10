# Problem: Count of Smaller Numbers After Self - https://leetcode.com/problems/count-of-smaller-numbers-after-self/

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n  
        indexed_nums = list(enumerate(nums))  
        def merge_sort(start, end, arr):
            if end - start == 1:
                return arr[start:end]

            mid = start + (end - start) // 2
            left = merge_sort(start, mid, arr)
            right = merge_sort(mid, end, arr)
            return merge(left, right)

        def merge(left, right):
            merged = []
            l = r = 0
            right_counter = 0  
            
            while l < len(left) and r < len(right):
                if left[l][1] <= right[r][1]:
                    result[left[l][0]] += right_counter  
                    merged.append(left[l])
                    l += 1
                else:
                    right_counter += 1
                    merged.append(right[r])
                    r += 1
            
            while l < len(left):
                result[left[l][0]] += right_counter
                merged.append(left[l])
                l += 1
            while r < len(right):
                merged.append(right[r])
                r += 1

            return merged

        merge_sort(0, n, indexed_nums)

        return result
