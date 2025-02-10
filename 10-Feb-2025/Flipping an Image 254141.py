# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in range(len(image)):
            l, r = 0, len(image[0])-1
            while l <= r:
                if image[row][r] and image[row][l]:
                    image[row][l], image[row][r] = 0, 0
                elif image[row][r] == 0 and image[row][l]:
                    image[row][l],image[row][r] = 1, 0
                elif image[row][r] and image[row][l] == 0:
                    image[row][r],image[row][l] = 1, 0
                else:
                    image[row][l], image[row][r] = 1, 1
                l += 1
                r -= 1
        return image