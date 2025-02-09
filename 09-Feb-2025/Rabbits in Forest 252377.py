# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        diction = Counter(answers)
        Sum = 0
        for i in diction:
            Sum += diction[i]
            if diction[i] % (i + 1):
                Sum -= ((diction[i] % (i + 1)) - (i + 1))
        return Sum