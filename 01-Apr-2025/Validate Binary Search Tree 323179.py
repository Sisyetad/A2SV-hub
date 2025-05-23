# Problem: Validate Binary Search Tree - https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return []
            
            return dfs(root.left) + [root.val] + dfs(root.right)
            
        result = dfs(root)
        for i in range(1, len(result)):
            if result[i - 1] >= result[i]:
                return False
        return True