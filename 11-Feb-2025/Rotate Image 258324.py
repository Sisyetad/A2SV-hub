# Problem: Rotate Image - https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        arr = list(zip(*copy.deepcopy(matrix)))
        n = len(matrix)
        for i in range(n):
            for j in range(len(matrix[0])):
                matrix[i][:] = arr[i][::-1]
        print(matrix)