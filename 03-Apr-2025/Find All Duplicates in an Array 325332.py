# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seeker = 0
        ans = []
        while seeker < len(nums):
            holder = nums[seeker] - 1
            if nums[holder] == nums[seeker]:
                seeker += 1
            else:
                nums[holder], nums[seeker] = nums[seeker], nums[holder]
        
        ans = []
        for i in range(len(nums)):
            if nums[i] != i+1:
                ans.append(nums[i])
        return ans