# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def validate(mid):
            count, sums = 1, 0
            for weight in weights:
                sums += weight
                if sums > mid:
                    count += 1
                    sums = weight
            return count <= days
        
        low, high = max(weights), sum(weights)
        ans = float('inf')
        while low <= high:
            mid = (low + high) // 2

            if validate(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans