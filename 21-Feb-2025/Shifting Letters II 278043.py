# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        s = [i for i in s]
        arr = [0] * n
        for i, j, dr in shifts:
            if dr:
                arr[i] += 1
                if j + 1 < len(arr):
                    arr[j+1] -= 1
            else:
                arr[i] -= 1
                if j + 1 < len(arr):
                    arr[j+1] += 1
        prefix_sum = 0
        for i in range(n):
            prefix_sum += arr[i]
            index = ((ord(s[i]) + prefix_sum - ord('a')) % 26)
            s[i] = chr(index + ord('a'))
        return "".join(s)