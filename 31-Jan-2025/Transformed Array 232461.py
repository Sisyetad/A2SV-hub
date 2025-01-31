# Problem: Transformed Array - https://leetcode.com/problems/transformed-array/description/

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        ans = [i for i in nums]
        index = 0
        for i in range(len(nums)):
            if nums[i] < 0:
                index = i - abs(nums[i])
                while index < -len(nums):
                    index = index + len(nums)
                ans[i] = nums[index]
            elif nums[i] > 0:
                index = i + nums[i]
                while index >= len(nums):
                    index = index - len(nums)
                ans[i] = nums[index]
            else:
                ans[i] = nums[i]
        return ans