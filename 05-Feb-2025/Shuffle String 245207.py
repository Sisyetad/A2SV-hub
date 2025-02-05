# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        arr = [0 for i in  range(len(indices))]
        j = 0
        for i in indices:
            arr[i] = s[j]
            j += 1
        return "".join(arr)