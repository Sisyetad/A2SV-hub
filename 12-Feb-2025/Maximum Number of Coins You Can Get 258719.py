# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        ans=0
        n=len(piles)
        r = n-1
        for i in range(n//3):
            ans+=piles[r-1]
            r-=2
        return ans