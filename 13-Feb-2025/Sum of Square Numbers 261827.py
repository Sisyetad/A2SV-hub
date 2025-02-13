# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a=0
        b=int(pow(c, 0.5))
        for i in range(int(pow(c,0.5))+1):
            if(pow(a,2) + pow(b,2) < (c)):
                a+=1
            elif(pow(a, 2) + pow(b,2) > (c)):
                b-=1
            else:
                return True
        return False