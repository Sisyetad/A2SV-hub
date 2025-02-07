# Problem: Majority Element II - https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        nums = Counter(nums)
        for key in nums:
            if nums[key] > n/3:
                ans.append(key)
        return ans