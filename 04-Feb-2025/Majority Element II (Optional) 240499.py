# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        nums = Counter(nums)
        for key in nums:
            if nums[key] > n/3:
                ans.append(key)
        return ans