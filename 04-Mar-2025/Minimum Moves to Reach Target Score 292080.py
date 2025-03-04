# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        while maxDoubles:
            if target % 2:
                if target > 1:
                    target -= 1
                    count += 1
                else:
                    break
            else:
                target //= 2
                maxDoubles -= 1
                count += 1
        return count + target - 1