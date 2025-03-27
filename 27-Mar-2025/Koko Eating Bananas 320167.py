# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isValid(mid):
            count = 0
            for pile in piles:
                if pile % mid:
                    count += 1
                count += pile // mid
            return count <= h

        mins, maxs = 1, max(piles) 
        ans = None
        while mins <= maxs:
            optimal = mins + (maxs - mins) // 2

            if isValid(optimal):
                ans = optimal
                maxs = optimal - 1
            else:
                mins = optimal + 1

        return ans