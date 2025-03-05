# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        L_count = Rcount = 0
        ans = 0
        for i in s:
            if i == 'L':
                L_count += 1
            else:
                Rcount += 1
            if L_count == Rcount:
                ans  += 1
                L_count = Rcount = 0
        return ans