# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        place = 0
        seeker = 1
        ans = 0
        s = [int(i) for i in s]
        while seeker < len(s):
            if s[place] == 0:
                place += 1
            elif s[seeker] == 0:
                s[place], s[seeker] = s[seeker], s[place]
                ans += seeker - place
                place += 1
            seeker += 1 
        return ans