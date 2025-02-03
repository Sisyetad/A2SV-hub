# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        n = len(ranges)
        tracker = set()
        checker = {i for i in range(left, right + 1)}
        for i in range(n):
            tracker = tracker | {i for i in range(ranges[i][0],ranges[i][-1] + 1)}
        return checker == checker & tracker