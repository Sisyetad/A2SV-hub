# Problem: Get Equal Substrings Within Budget - https://leetcode.com/problems/get-equal-substrings-within-budget/

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        window = 0
        left = 0
        size = 0
        for right in range(n):
            window += (abs(ord(s[right]) - ord(t[right])))
            while window > maxCost:
                window -= (abs(ord(s[left]) - ord(t[left])))
                left += 1
            size = max(size, right - left + 1)
        return size