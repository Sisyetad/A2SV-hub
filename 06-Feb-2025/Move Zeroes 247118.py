# Problem: Move Zeroes - https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        l,r=0,1
        while (l < n and r < n):
            if(nums[l]):
                l+=1
            if(nums[r]):
                nums[l],nums[r]=nums[r],nums[l]
            r+=1    