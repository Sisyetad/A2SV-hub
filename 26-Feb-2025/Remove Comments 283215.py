# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        in_block = False
        result = []
        buffer = []  

        for line in source:
            i = 0
            if not in_block:
                buffer = []  
            while i < len(line):
                if not in_block and i + 1 < len(line) and line[i:i+2] == "//":
                    break 
                elif not in_block and i + 1 < len(line) and line[i:i+2] == "/*":
                    in_block = True
                    i += 1 
                elif in_block and i + 1 < len(line) and line[i:i+2] == "*/":
                    in_block = False
                    i += 1 
                elif not in_block:
                    buffer.append(line[i]) 
                i += 1

            if buffer and not in_block:
                result.append("".join(buffer))  

        return result