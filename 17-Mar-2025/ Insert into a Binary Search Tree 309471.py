# Problem:  Insert into a Binary Search Tree - https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def helper(root, val):
            if not root.right and root.val < val:
                root.right = TreeNode(val)
            elif not root.left and root.val > val:
                root.left = TreeNode(val)
            elif root.val > val:
                helper(root.left,val)
            else:
                helper(root.right,val)
        
        if not root:
            root = TreeNode(val)
            return root
        helper(root, val)
        return root