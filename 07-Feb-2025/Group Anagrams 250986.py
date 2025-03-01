# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:    
        ans = defaultdict(list)
        print(ans)
        for s in strs:
            key = "".join(sorted(s))
            ans[key].append(s)
        
        return list(ans.values())