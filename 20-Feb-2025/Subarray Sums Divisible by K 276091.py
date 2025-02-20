# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        prefix_sum = 0
        ans = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            ans += prefix_count[prefix_sum % k]
            prefix_count[prefix_sum % k] += 1
        return ans