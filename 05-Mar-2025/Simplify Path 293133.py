# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split('/')
        for i in path:
            if i == '.' or i == '':
                continue
            elif i == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        
        return "/" + "/".join(stack)