# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        arr = [0] * n
        nums.sort(reverse = True)
        for i, j in requests:
            arr[i] += 1
            if j + 1 < n:
                arr[j+1] -= 1
        for i in range(1, n):
            arr[i] += arr[i-1]

        arr.sort(reverse = True)
        ans = 0
        left = 0
        for i in arr:
            ans += (i * nums[left])
            left += 1
        return ans%(pow(10,9) + 7)