# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

from array import array
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = array("i",range(1,n+1))
        i = 0
        while len(arr) != 1:
            print(arr.pop((i + k - 1) % n))
            i = (i + k - 1) % n
            n -= 1
        return arr[0]