# Problem: Max Consecutive Ones III - https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        window = 0
        left = 0
        window_count = 0
        for right in range(len(nums)):
            window_count += nums[right]
            if window_count + k >= right - left + 1:
                window = max(window, right - left + 1)
            else:
                window_count -= nums[left]
                left += 1
        return window
