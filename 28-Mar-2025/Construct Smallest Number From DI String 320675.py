# Problem: Construct Smallest Number From DI String - https://leetcode.com/problems/construct-smallest-number-from-di-string/description/

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        result = ''
        stack = []
        for i in range(1, len(pattern) + 2):
            stack.append(str(i))

            if i == len(pattern) + 1 or pattern[i - 1] == 'I':
                while stack:
                    result += stack.pop()

        return result