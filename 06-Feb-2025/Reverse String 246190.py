# Problem: Reverse String - https://leetcode.com/problems/reverse-string/description/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]
        '''i,j= 0,-1
        while i < len(s)+j:
            s[i],s[j] = s[j],s[i]
            i+=1
            j-=1'''

        return s