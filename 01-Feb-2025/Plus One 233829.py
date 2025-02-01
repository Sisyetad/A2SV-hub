# Problem: Plus One - https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        i = -1
        while i > -len(digits) and digits[i] > 9:
            digits[i] = 0
            i -= 1
            digits[i] += 1
        if i <= -len(digits) and digits[i] > 9:
            digits[0] = 0
            digits.insert(0,1)
        return digits