# Problem: H-Index - https://leetcode.com/problems/h-index/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations)
        ans = 0
        for i in range(len(citations)):
            if citations[i] <= len(citations) - i:
                ans = max(citations[i], ans)
            else:
                ans = max(len(citations) - i, ans)
        return ans