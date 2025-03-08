# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        n = len(s)
        for i in range(n):
            if s[i] == '#':
                if stack1:
                    stack1.pop()
            else:
                stack1.append(s[i])
        n = len(t)
        for j in range(n):
            if t[j] == '#':
                if stack2:
                    stack2.pop()
            else:
                stack2.append(t[j])
       
        return stack1 == stack2