# Problem: Sum of Subarray Minimums - https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        ans = 0
        i, n = 0, len(arr)
        arr.append(float('-inf'))
        while i <= n:
            while stack and stack[-1][0] > arr[i]:
                top = stack.pop()
                if stack:
                    ans += ((top[-1] - stack[-1][-1]) * (i - top[-1])) * top[0]
                else:
                    ans += ((top[-1] + 1) * (i - top[-1])) * top[0]

            stack.append((arr[i],i))
            i += 1
        return ans % (pow(10,9) + 7)