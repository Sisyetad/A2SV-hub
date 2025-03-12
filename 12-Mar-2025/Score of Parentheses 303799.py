# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for i in s:
            if i == '(':
                stack.append(0)
            else:
                top = stack.pop()
                if top:
                    if stack:
                        stack[-1] += (top * 2)
                    else:
                        stack.append(top * 2)
                else:
                    if stack:
                        stack[-1] += 1
                    else:
                        stack.append(1)
        return stack.pop()