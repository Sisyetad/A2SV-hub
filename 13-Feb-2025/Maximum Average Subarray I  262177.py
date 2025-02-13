# Problem: Maximum Average Subarray I  - https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = 0
        for i in range(k):
            curr_sum += nums[i]
        Max_sum = curr_sum
        for i in range(k,len(nums)):
            curr_sum -= (nums[i - k] - nums[i])
            Max_sum = max(Max_sum, curr_sum)
        return Max_sum / k