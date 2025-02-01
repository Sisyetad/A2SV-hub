# Problem: Roman to Integer - https://leetcode.com/problems/roman-to-integer/?envType=problem-list-v2&envId=string

class Solution:
    def romanToInt(self, s: str) -> int:
        arr = [0]
        for i in s:
            if i == 'I':
                arr.append(1)
            elif i == 'V':
                if arr[-1] == 1:
                    arr[-1] = 4
                else:
                    arr.append(5)
            elif i == 'X':
                if arr[-1] == 1:
                    arr[-1] = 9
                elif arr[-1] == 5:
                    continue
                else:
                    arr.append(10)
            elif i == 'L':
                if arr[-1] == 1:
                    arr[-1] = 49
                elif arr[-1] == 5:
                    arr[-1] = 45
                elif arr[-1] == 10:
                    arr[-1] = 40
                else:
                    arr.append(50)
            elif i == 'C':
                if arr[-1] == 1:
                    arr[-1] = 99
                elif arr[-1] == 5:
                    arr[-1] = 95
                elif arr[-1] == 10:
                    arr[-1] = 90
                elif arr[-1] == 50:
                    continue
                else:
                    arr.append(100)
            elif i == 'D':
                if arr[-1] == 1:
                    arr[-1] = 499
                elif arr[-1] == 5:
                    arr[-1] = 495
                elif arr[-1] == 10:
                    arr[-1] = 490
                elif arr[-1] == 50:
                    arr[-1] = 450
                elif arr[-1] == 100:
                    arr[-1] = 400
                else:
                    arr.append(500)
            elif i == 'M':
                if arr[-1] == 1:
                    arr[-1] = 999
                elif arr[-1] == 5:
                    arr[-1] = 995
                elif arr[-1] == 10:
                    arr[-1] = 990
                elif arr[-1] == 50:
                    arr[-1] = 950
                elif arr[-1] == 100:
                    arr[-1] = 900
                elif arr[-1] == 500:
                    continue
                else:
                    arr.append(1000)
        return sum(arr)