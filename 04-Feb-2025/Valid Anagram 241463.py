# Problem: Valid Anagram - https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s, t):
        new1 = sorted(s)
        new2 = sorted(t)
        if(new1==new2):
            return True
        return False