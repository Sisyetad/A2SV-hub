# Problem: First Bad Version - https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start, end = 0, n
        ans = -1
        while start <= end:
            mid = start + (end - start) // 2
            if not isBadVersion(mid):
                start = mid + 1
            if isBadVersion(mid):
                ans = mid
                end = mid - 1
        return ans