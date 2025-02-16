# Problem: 3Sum Closest  - https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        Sum = float('inf')
        min_diff = float('inf')
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if min_diff > abs(nums[right] + nums[left] + nums[i] - target):
                    min_diff = abs(nums[right] + nums[left] + nums[i] - target)
                    Sum = nums[right] + nums[left] + nums[i]
                if nums[right] + nums[left] + nums[i] < target:
                    left += 1
                elif nums[right] + nums[left] + nums[i] > target:
                    right -= 1
                else:
                    return nums[right] + nums[left] + nums[i]
        return Sum