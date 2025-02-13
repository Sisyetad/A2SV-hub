# Problem: Find All Anagrams in a String  - https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Result array to store starting indices of anagrams
        result = []
        k = len(p)
        if len(s) < k:
            return result
        target = Counter(p)
        window = Counter()
        for i in range(k):
            window[s[i]] += 1
        for i in range(k, len(s)):
            if target == window:
                result.append(i-k)
            window[s[i]] += 1
            window[s[i-k]] -= 1
            if window[s[i-k]] == 0:
                del window[s[i-k]]
        if target == window:
            result.append(i + 1 - k)
        return result