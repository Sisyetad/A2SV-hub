# Problem: Minimum Size Subarray Sum - https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        Sum = 0
        ans = len(nums) + 1
        for right in range(len(nums)):
            Sum += nums[right]
            while Sum >= target:
                ans = min(ans, right - left + 1)
                Sum -= nums[left]
                left += 1
        return ans if ans != len(nums) + 1 else 0