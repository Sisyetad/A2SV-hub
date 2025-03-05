# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        diction = Counter(s)
        num = 1
        while diction['1'] > 1:
            num = (num * 10) + 1
            diction['1'] -= 1
        num *= pow(10, diction['0'])
        num = (num * 10) + 1
        return str(num)[1:]