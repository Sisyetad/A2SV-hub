# Problem: Grid Game - https://leetcode.com/problems/grid-game/

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        
        top_prefix = [0] * n
        bottom_prefix = [0] * n
        
        top_prefix[0] = grid[0][0]
        bottom_prefix[0] = grid[1][0]
        
        for j in range(1, n):
            top_prefix[j] = top_prefix[j - 1] + grid[0][j]
            bottom_prefix[j] = bottom_prefix[j - 1] + grid[1][j]

        min_second_player = float('inf')
        
        for j in range(n):
            top_remaining = top_prefix[n - 1] - top_prefix[j]  
            bottom_remaining = bottom_prefix[j - 1] if j > 0 else 0  
            
            second_player_score = max(top_remaining, bottom_remaining)
            min_second_player = min(min_second_player, second_player_score)
        
        return min_second_player
