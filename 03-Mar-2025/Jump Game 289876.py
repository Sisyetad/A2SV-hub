# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end = 0
        n = len(nums)
        for i in range(n):
            if i > end:
                return False
            end = max(end, i + nums[i])
        return True