# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = []
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if row + col >= len(ans):
                    ans.append([])
                if not (row + col)%2:
                    ans[row + col].insert(0,mat[row][col])
                else:
                    ans[row + col].append(mat[row][col])
        ans = [i for row in ans for i in row]
        return ans