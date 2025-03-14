# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def combs(rowIndex,k):
            return fact(rowIndex)//(fact(k) * fact(rowIndex - k))
        def fact(n):
            if n == 1 or n == 0:
                return 1
            return n * fact(n-1)
        return [combs(rowIndex, k) for k in range(rowIndex + 1)]
        #pascals triangle is the cofficient with combination