# Problem: Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/submissions/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counter = Counter(t)
        s_counter = Counter()
        left = 0
        valid_count = 0
        size = len(s) + 1
        ans = [-1,-1]
        if len(t) > len(s):
            return ""

        for right in range(len(s)):
            if s[right] in t_counter:
                s_counter[s[right]] += 1
                if s_counter[s[right]] == t_counter[s[right]]:
                    valid_count += 1
            while valid_count == len(t_counter):
                if size > right - left + 1:
                    ans = [left, right]
                    size = right - left + 1
                if s[left] in t_counter:
                    s_counter[s[left]] -= 1
                    if s_counter[s[left]] < t_counter[s[left]]:
                        valid_count -= 1
                left += 1
            
        return  s[ans[0]:ans[-1] + 1]