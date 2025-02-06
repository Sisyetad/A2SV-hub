# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        i,j = 0,1
        while i < len(nums) and j < len(nums):
            if nums[i]:
                i += 1
            if nums[j]:
                nums[i],nums[j] = nums[j],nums[i]
            j += 1
        return nums