# Problem: Check if All Characters Have Equal Number of Occurrences - https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        n = len(s)
        s = Counter(s)
        occurance = n/len(s)
        for key in s:
            if s[key] != occurance:
                return False
        return True