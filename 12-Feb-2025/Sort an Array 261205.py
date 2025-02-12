# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        maxs = max(nums)
        mins = min(nums)
        ans = []
        arr = [0] * (maxs - mins + 1)
        for num in nums:
            arr[num - mins] += 1
        for i in range(len(arr)):
            ans.extend([i + mins] * arr[i])
        return ans