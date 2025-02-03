# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses/

from collections import Counter
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losers = Counter([j[-1] for j in matches])
        winners = Counter([j[0] for j in matches])
        return [sorted([key for key in winners.keys() - losers.keys()]),sorted([key for key in losers if losers[key] == 1])]