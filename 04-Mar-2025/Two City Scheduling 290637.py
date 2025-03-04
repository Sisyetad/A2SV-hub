# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        arr = []
        for i, cost in enumerate(costs):
            arr.append((cost[-1] - cost[0],i))
        arr.sort()
        n = len(arr)
        total = 0
        for i in range(n):
            if i < n//2:
                total += costs[arr[i][-1]][-1]
            else:
                total += costs[arr[i][-1]][0]
        return total