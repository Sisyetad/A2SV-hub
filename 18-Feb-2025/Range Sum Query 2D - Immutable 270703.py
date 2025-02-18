# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        for row in matrix:
            ac = 0
            for col in range(1, len(row)):
                ac = row[col - 1]
                row[col] += ac
        for row in range(len(matrix[0])):
            ac = 0
            for col in range(1, len(matrix)):
                ac = matrix[col - 1][row]
                matrix[col][row] += ac
    
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:  
        if row1 == 0 and col1 == 0:
            return self.matrix[row2][col2]
        elif col1 == 0:
            return self.matrix[row2][col2] - self.matrix[row1 - 1][col2]
        elif row1 == 0:
            return self.matrix[row2][col2] - self.matrix[row2][col1 - 1]
        else:
            return self.matrix[row2][col2] - (self.matrix[row1 - 1][col2] + self.matrix[row2][col1 - 1]) + self.matrix[row1 - 1][col1 - 1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)