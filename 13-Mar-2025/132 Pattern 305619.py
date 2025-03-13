# Problem: 132 Pattern - https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        #abc
        mono_stack = []
        c = float('-inf')
        for a in reversed(nums):
            if a < c:
                return True
            while mono_stack and mono_stack[-1] < a:
                c = mono_stack.pop()
            mono_stack.append(a)
        return False