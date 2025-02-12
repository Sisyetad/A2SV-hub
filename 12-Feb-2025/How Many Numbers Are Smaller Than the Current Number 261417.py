# Problem: How Many Numbers Are Smaller Than the Current Number - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        x = min(nums)
        y = max(nums)
        preCount = [0] * (y - x + 1)
        ans = []
        for i in nums:
            preCount[i-x] += 1
        for i in nums:
            ans.extend([sum(preCount[:i - x])])
        return ans