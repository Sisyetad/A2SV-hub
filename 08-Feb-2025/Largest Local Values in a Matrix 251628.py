# Problem: Largest Local Values in a Matrix - https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n, res = len(grid), []

        for row in range(1, n - 1):
            arr = []
            for col in range(1, n - 1):
                Max = 0

                for k in range(-1, 2):
                    for l in range(-1,2):
                        Max = max(Max, grid[row+k][col+l])

                arr.append(Max)
            res.append(arr)

        return res