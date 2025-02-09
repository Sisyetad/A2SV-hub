# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        mat = [[0 for i in range(len(matrix))] for i in range(len(matrix[0]))]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                mat[col][row] = matrix[row][col]
        return mat