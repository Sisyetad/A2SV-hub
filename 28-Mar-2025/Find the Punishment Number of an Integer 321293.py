# Problem: Find the Punishment Number of an Integer - https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description/

class Solution:
    def punishmentNumber(self, n: int) -> int:
        def backtrack(sqr_num, target, i, curr) -> bool:
            m = len(sqr_num)
            if i == m:
                return target == curr
                
            for j in range(i, m):
                new_curr = curr + int(sqr_num[i : j + 1])

                if new_curr > target:
                    break
                if backtrack(sqr_num, target, j + 1, new_curr):
                    return True
            return False
        ans = 0
        for num in range(1, n + 1):
            sqr_num = num * num
            if backtrack(str(sqr_num), num, 0, 0):
                ans += sqr_num
        return ans