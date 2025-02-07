# Problem: Integer to Roman - https://leetcode.com/problems/integer-to-roman/description/

class Solution:
    def intToRoman(self, num: int) -> str:
        diction = {1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'} 
        ans = []
        while num % 1 != num:
            for i in diction:
                if num // i:
                    for j in range(num // i):
                        ans.append(diction[i])
                        num %= i
        return "".join(ans)