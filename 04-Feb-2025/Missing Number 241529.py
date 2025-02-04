# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = set(nums)
        Set = set(range(len(nums)+1))
        return list(Set - nums)[0]
