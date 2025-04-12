# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        pos = -1
        start = 0
        end = len(matrix) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if matrix[mid][0] <= target:
                pos = mid
                start = mid + 1
            else:
                end = mid - 1

        row = matrix[pos]      
        start, end = 0, len(row) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if row[mid] < target:
                start = mid + 1
            
            elif row[mid] > target:
                end = mid - 1
            
            else:
                return True
            
        return False
