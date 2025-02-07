# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = Counter(nums)
        no_pair = 0
        for i in nums:
            if nums[i] % 2:
                no_pair += 1
        return [(n - no_pair) // 2, no_pair]