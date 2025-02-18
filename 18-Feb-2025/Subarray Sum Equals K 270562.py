# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

from collections import Counter 
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        cumulative_sum = 0
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1
        for num in nums:
            cumulative_sum += num
            count += prefix_sums[cumulative_sum - k]
            prefix_sums[cumulative_sum] += 1
        return count