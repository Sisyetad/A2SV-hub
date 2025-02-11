# Problem: Spiral Matrix - https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        directions = [(0,1), (1,0), (0, -1), (-1, 0)]
        n = len(matrix) * len(matrix[0])
        dir_index = 0
        (x, y) = (0, -1)
        ans = []
        while len(ans) < n:
            r, c = x + directions[dir_index][0], y + directions[dir_index][1]
            while r < len(matrix) and c < len(matrix[0]) and matrix[r][c] != '*':
                ans.append(matrix[r][c])
                matrix[r][c] = '*'
                x, y = r, c
                r, c = x + directions[dir_index][0], y + directions[dir_index][1] 
            dir_index = (dir_index + 1) % 4
        
        return ans