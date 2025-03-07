# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_que = deque()
        min_que = deque()
        n = len(nums)
        left = 0
        max_len = 0
        for right in range(n):
            while max_que and max_que[-1] < nums[right]:
                max_que.pop()
            max_que.append(nums[right])
        
            while min_que and min_que[-1] > nums[right]:
                min_que.pop()
            min_que.append(nums[right])

           
            while max_que[0] - min_que[0] > limit:
                if nums[left] == max_que[0]:
                    max_que.popleft()
                if nums[left] == min_que[0]:
                    min_que.popleft()
                left += 1  
            max_len = max(max_len, right - left + 1)

        return max_len