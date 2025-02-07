# Problem: All Divisions With the Highest Score of a Binary Array - https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/

from array import array
class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums_left, nums_right = 0,0
        arr = array("i")
        last = []
        for i in nums:
            if i == 1:
                nums_right += 1
        ans = nums_left + nums_right
        arr.append(nums_left + nums_right)
        for i in range(n):
            if nums[i]:
                nums_right -= 1
            else:
                nums_left += 1
            ans = max(ans,nums_left + nums_right)
            arr.append(nums_left + nums_right)
        for i in range(len(arr)):
            if ans == arr[i]:
                last.append(i)
        return last