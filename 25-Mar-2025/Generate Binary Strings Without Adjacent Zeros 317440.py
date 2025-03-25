# Problem: Generate Binary Strings Without Adjacent Zeros - https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/

class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = set()
        def helper(n, path, bit):
            if n == 0:
                res.add(''.join(path))
                return
            
            path.append(str(bit))
            if path and path[-1] != '0' or bit:
                helper(n-1, path, bit)

            if path and path[-1] != '0' or not bit:
                helper(n-1, path, abs(bit-1))
            path.pop()
            
        helper(n,[],1)
        helper(n,[],0)

        return list(res)