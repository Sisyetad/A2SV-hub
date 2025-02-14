# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target=Counter(s1)
        k=len(s1)
        n=len(s2)
        window=Counter(s2[:k])
        for i in range(k,n):
            if target == window:
                return True
            window[s2[i-k]]-=1
            window[s2[i]]+=1
            if window[s2[i-k]]==0:
                del window[s2[i-k]]
        if target == window:
                return True
        return False