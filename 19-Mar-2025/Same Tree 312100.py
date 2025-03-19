# Problem: Same Tree - https://leetcode.com/problems/same-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        i=0
        def helper(root,i):
            if not root:
                return []
            i+=1
            return helper(root.left,i) + [(root.val,i)] + helper(root.right,i)
        p = helper(p,i)
        q = helper(q,i)
        
        if p == q:
            return True
        return False