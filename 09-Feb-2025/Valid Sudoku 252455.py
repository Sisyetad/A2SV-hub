# Problem: Valid Sudoku - https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(len(board)):
            row_diction = Counter(board[row][:])
            for i in row_diction:
                if i != "." and row_diction[i] > 1:
                    return False
        for col in range(len(board[0])):
            col_diction = {}
            for row in range(len(board)):
                if board[row][col] not in col_diction:
                    col_diction[board[row][col]] = 0
                col_diction[board[row][col]] += 1
            for i in col_diction:
                if i != "." and col_diction[i] > 1:
                    return False
        for row in range(0,len(board),3):
            for col in range(0,len(board[0]),3):
                sub_box = {}
                for i in range(row,row + 3):
                    for j in range(col, col + 3):
                        if 0 <= i < len(board) and 0 <= j < len(board[0]):
                            if board[i][j] not in sub_box:
                                sub_box[board[i][j]] = 0
                            sub_box[board[i][j]] += 1
                for i in sub_box:
                    if i != '.' and sub_box[i] > 1:
                        return False
        return True