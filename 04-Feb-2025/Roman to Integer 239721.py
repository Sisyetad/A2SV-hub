# Problem: Roman to Integer - https://leetcode.com/problems/roman-to-integer/?envType=problem-list-v2&envId=string

class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        Sum = 0
        pre = 0
        for i in s:
            if dic[i] > pre:
                Sum = Sum + (dic[i] - (2 * pre))
                pre = dic[i]
            else:
                Sum += dic[i]
                pre = dic[i]
        return Sum