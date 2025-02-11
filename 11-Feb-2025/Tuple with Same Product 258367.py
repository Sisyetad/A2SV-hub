# Problem: Tuple with Same Product - http://leetcode.com/problems/tuple-with-same-product

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        diction = defaultdict(int)
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                diction[nums[i] * nums[j]] += 1
        Sum = 0
        for i in diction.values():
            if i > 1:
                Sum += ((i*(i-1)//2) * 8)
                
        return Sum
