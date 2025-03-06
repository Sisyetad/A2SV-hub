# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        mono_stack = []
        n = len(temp)
        ans = [0]*n
        
        for i in range(n):
            while mono_stack and mono_stack[-1][0] < temp[i]:
                top = mono_stack.pop()
                ans[top[-1]] = i - top[-1]
            mono_stack.append((temp[i],i))
        return ans