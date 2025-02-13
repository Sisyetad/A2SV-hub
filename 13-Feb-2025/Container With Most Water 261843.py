# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n-1
        area = (right - left) * min(height[left], height[right])
        while(left < right):
            h = min( height[left], height[right])
            width = right - left
            if(height[left] < height[right]):
                left += 1
            else:
                right -= 1
            area = max(area, width * h)
        return area