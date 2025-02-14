# Problem: Maximum Points You Can Obtain from Cards - https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        min_sum = 0
        n = len(cardPoints)
        total_sum = sum(cardPoints)
        for i in range(n - k):
            min_sum += cardPoints[i]
        window = min_sum
        left = 0
        for right in range(n - k, n):
            window += cardPoints[right] - cardPoints[left]
            min_sum = min(min_sum, window)
            left += 1
        return total_sum - min_sum