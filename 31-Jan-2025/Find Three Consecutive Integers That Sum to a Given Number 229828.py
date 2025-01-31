# Problem: Find Three Consecutive Integers That Sum to a Given Number - https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        ans = []
        x = num / 3
        if x != num // 3:
            return ans
        else:
            for i in [x - 1, x, x + 1]:
                ans.append(int(i))
        return ans