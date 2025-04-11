# Problem: Create Sorted Array through Instructions - https://leetcode.com/problems/create-sorted-array-through-instructions/

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        arr = []
        result = 0
        MOD = 10**9 + 7

        for i, num in enumerate(instructions):
            left = bisect_left(arr, num)
            right = len(arr) - bisect_right(arr, num)

            result += min(left, right)
            result %= MOD

            insort(arr, num)  

        return result
