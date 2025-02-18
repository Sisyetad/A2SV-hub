# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * (len(nums))
        prefix, suffix = 1, 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]
        for i in range(1, len(nums) + 1):
            output[-i] *= suffix
            suffix *= nums[-i]
        return output