# Problem: Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution:
    def frequencySort(self, s: str) -> str:
        s = Counter(s)
        s = sorted(s.items(),key = lambda i:i[1])
        chars = []
        for i in s[::-1]:
            i = list(i)
            while i[1]:
                chars.append(i[0])
                i[1] -= 1
        return "".join(chars)