# Problem: Longest Repeating Character Replacement - https://leetcode.com/problems/longest-repeating-character-replacement/


from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = Counter()
        left, right = 0, 0
        counter = 0
        ans = 0
        while left < len(s) and right < len(s):
            window[s[right]] += 1
            counter = max(window[s[right]], counter)
            right += 1
            if right - left - counter <= k:
                ans = max(ans, right - left)
            else:
                window[s[left]] -= 1
                left += 1
        return ans