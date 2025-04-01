# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        diction = Counter(nums)
        freq = sorted(diction.items(), key = lambda x: x[1])
        
        for i in range(1, k + 1):
            ans.append(freq[-i][0])
        return ans
        