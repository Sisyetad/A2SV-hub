# Problem: Determine Whether Matrix Can Be Obtained By Rotation - https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        arr = copy.deepcopy(mat)
        for rotate in range(4):
            for i in range(len(mat)):
                for j in  range(len(mat)):
                    arr[i][j] = mat[-(j+1)][i]
                if mat == target:
                    return True
            mat = [row[:] for row in arr]
        return False