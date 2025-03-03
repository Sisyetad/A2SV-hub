# Problem: Contiguous Array - https://leetcode.com/problems/contiguous-array/

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        hashmap = {0:-1}
        prefix = 0
        ans = 0
        for i in range(n):
            if nums[i] == 0:
                prefix -= 1
            else:
                prefix += 1
            if prefix in hashmap:
                ans = max(ans, i - hashmap[prefix])
            else:
                hashmap[prefix] = i
        return ans