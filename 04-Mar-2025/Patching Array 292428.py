# Problem: Patching Array - https://leetcode.com/problems/patching-array/

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        prefix = 0
        nums.sort()
        count = 0
        i = 0
        while prefix < n:
            if i < len(nums) and prefix + 1 >= nums[i]:
                prefix += nums[i]
                i += 1
            else:
                prefix = (prefix * 2) + 1
                count += 1
                
        return count 