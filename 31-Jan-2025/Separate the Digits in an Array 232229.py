# Problem: Separate the Digits in an Array - https://leetcode.com/problems/separate-the-digits-in-an-array/description/

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        index = -1
        for num in nums[::-1]:
            while num % 10 != num:
                ans.insert(index, num % 10)
                index -= 1
                num //= 10
            else:
                ans.insert(index, num)
                index -= 1
        return ans