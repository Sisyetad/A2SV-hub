# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(bit: str) -> str:
            return '1' if bit == '0' else '0'
        
        def findBit(n, k):
            if n == 1:
                return '0'
            length = (2**n) - 1 
            mid = (length // 2) + 1  
            
            if k == mid:
                return '1'
            elif k < mid:
                return findBit(n - 1, k)
            else:
                return invert(findBit(n - 1, length - k + 1))
        
        return findBit(n, k)