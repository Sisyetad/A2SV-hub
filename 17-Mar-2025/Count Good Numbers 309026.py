# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution:
    def __init__(self):
        self.Mod = pow(10,9)+7
    def power(self, base, exp):
        if exp == 0:
            return 1
        a = b = self.power(base, exp//2) % self.Mod
        if exp % 2:
            b = (a * base) % self.Mod
        return (a * b) % self.Mod
    def countGoodNumbers(self, n: int) -> int:
        if n % 2:
            return (self.power(20,n//2) * 5) % self.Mod
        else:
            return self.power(20,n//2) % self.Mod