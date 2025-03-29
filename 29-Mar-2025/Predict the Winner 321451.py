# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return True
        def helper(nums, turn, scoreA, scoreB):
            if len(nums) == 2:
                if turn % 2:
                    return scoreB + max(nums) <= scoreA + min(nums)
                return scoreA + max(nums) >= scoreB + min(nums)

            if turn % 2:
                return (
                    helper(nums[1:], turn + 1, scoreA, scoreB + nums[0]) and
                    helper(nums[:-1], turn + 1, scoreA, scoreB + nums[-1])
                )
            else:
                return (
                    helper(nums[1:], turn + 1, scoreA + nums[0], scoreB) or
                    helper(nums[:-1], turn + 1, scoreA + nums[-1], scoreB)
                )

        return helper(nums, 0, 0, 0)
