# Problem: Largest Number - https://leetcode.com/problems/largest-number/

from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x, y):
            return 1 if x + y < y + x else -1 

        nums_str = list(map(str, nums))
        nums_str.sort(key=cmp_to_key(compare))
        result = "".join(nums_str)

        return "0" if result[0] == "0" else result
