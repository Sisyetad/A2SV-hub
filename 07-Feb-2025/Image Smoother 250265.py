# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        ans = [row[:] for row in img]
        n,n_arr = len(img),len(img[0])
        for row in range(n):
            for col in range(n_arr):
                Sum = 0
                count = 0
                for i in range(-1,2):
                    for j in range(-1,2):
                        if (row+i >= 0 and col+j >= 0) and (row+i  < n and col+j < n_arr):
                            Sum += img[row+i][col+j]
                            count += 1
                ans[row][col] = Sum//count

        return ans
