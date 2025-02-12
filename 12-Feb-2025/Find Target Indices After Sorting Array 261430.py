# Problem: Find Target Indices After Sorting Array - https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        mins = min(nums)
        maxs = max(nums)
        arr = [0] * (maxs - mins + 1)
        ans = []
        for i in nums:
            arr[i - mins] += 1
        nums = []
        for i in range(len(arr)):
            nums.extend([i + mins] * arr[i])
        for i in range(len(nums)):
            if nums[i] == target:
                ans.append(i)
        return ans