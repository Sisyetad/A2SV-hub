# Problem: Number of Islands - https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def inBound(x, y):
            return (0 <= x < len(grid) and 0 <= y < len(grid[0]))
        
        visited = [[False for i in range(len(grid[0]))] for i in range(len(grid))]
        def dfs(x, y):
            if not inBound(x, y) or grid[x][y] == '0' or visited[x][y]:
                return
            
            visited[x][y] = True
            for x_chg, y_chg in directions:
                x_new, y_new = x - x_chg, y - y_chg
                dfs(x_new, y_new)
        ans = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1' and not visited[row][col]:
                    dfs(row, col)
                    ans += 1
        return ans