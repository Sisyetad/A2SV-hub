# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        prefix = 0
        n = len(nums)
        mins = maxs = 0
        
        for i in range(n):
            prefix += nums[i]
            maxs = max(maxs, prefix)
            mins = min(mins, prefix)
            
        return maxs - mins