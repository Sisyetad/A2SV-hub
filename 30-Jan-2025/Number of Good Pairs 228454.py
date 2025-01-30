# Problem: Number of Good Pairs - https://leetcode.com/problems/number-of-good-pairs/

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = {}
        result=0
        for i in nums:
            if i not in ans:
                ans[i] = [1,0]
            else:
                ans[i][1] = ans[i][0] + ans[i][1]
                ans[i][0] += 1
        for i in ans:
            result += ans[i][1]
        print(ans)
        return result