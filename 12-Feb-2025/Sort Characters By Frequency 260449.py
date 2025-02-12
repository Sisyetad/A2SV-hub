# Problem: Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution:
    def frequencySort(self, s: str) -> str:
        s = Counter(s)
        s = sorted(s.items(),key = lambda i:i[1])
        arr = []
        for i in s[::-1]:
            i = list(i)
            while i[1]:
                arr.append(i[0])
                i[1] -= 1
        return "".join(arr)