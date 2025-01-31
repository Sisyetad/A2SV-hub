# Problem: Goal Parser Interpretation - https://leetcode.com/problems/goal-parser-interpretation/description/

class Solution:
    def interpret(self, command: str) -> str:
        result=""
        for i in command:
            if i == ')':
                removed = result[-1]
                if removed == '(':
                    result = result[:-1] + 'o'
                else:
                    result = result[:-3] + "al"
            else:
                result += i
        return result