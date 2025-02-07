# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:       
        Sum = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                Sum += nums[i]
        ans = []
        for i in range(len(queries)):
            if nums[queries[i][1]] % 2 == 0:
                Sum -= nums[queries[i][1]]
            if (nums[queries[i][1]] + queries[i][0]) % 2 == 0:
                Sum += nums[queries[i][1]] + queries[i][0]
            nums[queries[i][1]] += queries[i][0]
            ans.append(Sum)
        return ans
        

    