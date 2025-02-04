# Problem: Find Duplicate File in System - https://leetcode.com/problems/find-duplicate-file-in-system/

import re
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = {}
        for i in paths:
            i = i.split(" ")
            for j in range(1,len(i)):
                myfile = "/".join([i[0], i[j]])
                file_content = tuple(re.findall(r'\((.*?)\)', myfile))
                if file_content not in dic:
                    dic[file_content] = []
                dic[file_content].append(re.sub(r'\(.*?\)', '', myfile).strip())
        return [group for group in dic.values() if len(group) > 1]
