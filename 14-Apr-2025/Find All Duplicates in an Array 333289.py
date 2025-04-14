# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seeker = 0
        while seeker < len(nums):
            correct_position = nums[seeker] - 1
            if nums[correct_position] == nums[seeker]:
                seeker += 1
            else:
                nums[correct_position], nums[seeker] = nums[seeker], nums[correct_position]

        ans = []
        for i in range(len(nums)):
            if nums[i] != i+1:
                ans.append(nums[i])
        return ans