# Problem: Rotate String - https://leetcode.com/problems/rotate-string/

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(goal) != len(s):
            return False
        i=0
        while s != goal and i < len(s):
            s = s[1:] + s[0]
            i += 1
        else:
            return s == goal