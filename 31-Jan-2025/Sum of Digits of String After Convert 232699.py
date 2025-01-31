# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/description/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        alp_num = ""
        for i in s:
            alp_num += str(ord(i) - 96)
        num = int(alp_num)
        for i in range(k):
            sum = 0
            while num % 10 != num:
                sum += num % 10
                num //= 10
            num = sum +num
        return num