# Problem: Longest Nice Substring - https://leetcode.com/problems/longest-nice-substring/

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        s_set = set(s)

        for i, char in enumerate(s):
            if char.swapcase() not in s_set:
                s1 = self.longestNiceSubstring(s[0 : i])
                s2 = self.longestNiceSubstring(s[i + 1 :])
                return s2 if len(s2) > len(s1) else s1
        
        return s