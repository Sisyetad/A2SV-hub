# Problem: 3Sum - https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = set()
        for i in range(len(nums)):
            target = 0 - nums[i]
            left = i + 1
            right = len(nums)-1
            while left < right:
                if nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    ans.add((nums[i],nums[left], nums[right]))
                    left += 1
                    right -= 1
        result = []
        for i in ans:
            result.append(list(i))
        return result