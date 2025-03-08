# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack=[]
        for i in logs:
            if(i=="../"):
                if stack:
                    stack.pop(-1)
            elif(i == "./"):
                continue
            else:
                stack.append(i)
        return len(stack)