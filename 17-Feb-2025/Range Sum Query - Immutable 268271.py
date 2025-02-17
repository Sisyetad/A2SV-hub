# Problem: Range Sum Query - Immutable - https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.cum = 0
        for i in range(len(self.nums)):
            self.nums[i], self.cum = self.cum, self.cum + self.nums[i]
        self.nums.append(self.cum)

    def sumRange(self, left: int, right: int) -> int:
        self.left = left
        self.right = right
        return self.nums[self.right + 1] - self.nums[self.left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)