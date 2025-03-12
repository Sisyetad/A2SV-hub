# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operation = {'*', '/', '+', '-'}
        for i in tokens:
            if i not in operation:
                stack.append(int(i))
            else:
                top = stack.pop()
                if i == '*':
                    stack[-1] *= top
                elif i == '+':
                    stack[-1] += top
                elif i == '-':
                    stack[-1] -= top
                else:
                    x = int(stack.pop()/top)
                    stack.append(x) 
                
        return stack.pop()