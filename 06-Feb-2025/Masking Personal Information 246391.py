# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskPII(self, s: str) -> str:
        s = s.lower()
        arr = []
        if s[-1].isalpha():
            return s[0] + "*" * 5 + str(s[s.index('@')-1:])
        else:
            for i in s[-len(s):]:
                if i.isalnum():
                    arr.append(i)
        arr = ['*'] * (len(arr)-4) + arr[-4:]
        if len(arr) > 10:
            arr.insert(0,'+')
        arr.insert(-4,'-')
        i = -8
        while i > -len(arr) + 1:
            arr.insert(i,'-')
            i -= 4
        return "".join(arr)