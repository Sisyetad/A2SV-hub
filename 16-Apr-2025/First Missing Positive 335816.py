# Problem: First Missing Positive - https://leetcode.com/problems/first-missing-positive/description/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            pos = nums[i] - 1
            if 0 <= pos < len(nums) and nums[i] != nums[pos]:
                nums[pos], nums[i] = nums[i], nums[pos]
            else:
                i += 1
                 
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1