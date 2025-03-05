# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        n = len(points)
        right = -1
        ans = 0
        for i in range(1,n+1):
            if points[-i][-1] < points[right][0]:
                right = -i
            if -i == right:
                ans += 1
        return ans