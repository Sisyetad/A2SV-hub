# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        buckets = [0] * (len(nums) + 1)
        for num in nums:
            buckets[num] += 1
        for i in range(len(nums) + 1):
            if buckets[i] == 0:
                return i