# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def inBound(x, y):
            if (0 <= x < len(grid)) and (0 <= y < len(grid[0])):
                return True
            return False

        visited = [[False for i in range(len(grid[0]))] for i in range(len(grid))]
        def dfs(x, y):
            if not inBound(x, y) or grid[x][y] == 0:
                return 1
            if visited[x][y]:
                return 0

            visited[x][y] = True
            perimeter = 0
            for x_chg, y_chg in directions:
                x_new, y_new = x - x_chg, y - y_chg
                perimeter += dfs(x_new, y_new)
            return perimeter
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i, j)
        return 0