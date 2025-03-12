# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == -1:
            return 1/x
        if n == 0:
            return 1

        if n % 2:
            a = self.myPow(x, n//2)
            b = a * x
        else:
            a = b = self.myPow(x, n//2)
        return a * b