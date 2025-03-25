# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str, last_val: int = None) -> bool:
        # Base case, remaining string is a valid solution
        if last_val and int(s) == last_val - 1:
            return True

        for i in range(1, len(s)):
            cur = int(s[:i])
            
            print(last_val)
            if last_val is None or cur == last_val - 1:
                if self.splitString(s[i:], cur):
                    return True

        return False