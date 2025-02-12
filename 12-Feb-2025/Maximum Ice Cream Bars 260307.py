# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        Max = max(costs)
        Min = min(costs)
        diction = {}
        for i in range(Min,Max+1):
            diction.setdefault(i, 0)
        for i in costs:
            diction[i] += 1
        index = 0
        Sum = 0
        for i in diction:
            while diction[i] > 0 and Sum + i <= coins:
                Sum += i
                index += 1
                diction[i] -= 1
        return index