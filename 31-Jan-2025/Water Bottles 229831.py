# Problem: Water Bottles - https://leetcode.com/problems/water-bottles/description

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans=0
        while numBottles >= numExchange:
            numBottles -= (numExchange - 1)
            ans += numExchange
        return ans + numBottles