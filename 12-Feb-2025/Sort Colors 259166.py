# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        diction = {0:0,1:0,2:0}
        for i in nums:
            diction[i] += 1
        index = 0
        for i in diction:
            while diction[i]:
                nums[index] = i
                index += 1
                diction[i] -= 1
            