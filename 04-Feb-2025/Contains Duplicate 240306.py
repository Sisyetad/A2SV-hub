# Problem: Contains Duplicate - https://leetcode.com/problems/contains-duplicate/description/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums = Counter(nums)
        for key in nums:
            if nums[key] > 1:
                return True
        return False