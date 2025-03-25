# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def helper(root, min_val, max_val):
            if not root:
                return max_val - min_val
            min_val = min(min_val, root.val)
            max_val = max(max_val, root.val)
            left_diff = helper(root.left, min_val, max_val)
            right_diff = helper(root.right, min_val, max_val)
            return max(left_diff, right_diff)
        return helper(root, root.val, root.val)