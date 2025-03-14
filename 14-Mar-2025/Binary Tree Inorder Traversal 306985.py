# Problem: Binary Tree Inorder Traversal - https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.arr = []
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return self.arr

        self.inorderTraversal(root.left)
        self.arr.append(root.val)
        self.inorderTraversal(root.right)
        return self.arr