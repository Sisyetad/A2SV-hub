# Problem: Find Original Array From Doubled Array (Optional) - https://leetcode.com/problems/find-original-array-from-doubled-array/

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        C = changed
        C.sort()
        H = Counter(C)
        ans = []
        for c in C:
            if H[c]:
                H[c] -= 1
                if H.get(c+c, 0) > 0:
                    H[c+c] -= 1
                    ans.append(c)
                else:
                    return []
        return ans