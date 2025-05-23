# Problem: Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        if not root.left and not root.right and root.val == key:
            return None
        elif not root.left and root.val == key:
            return root.right
        elif not root.right and root.val == key:
            return root.left
        elif root.val == key:
            curr = root.right
            if curr.left:
                while curr.left:
                    curr = curr.left
                root.val = curr.val
                root.right = self.deleteNode(root.right, curr.val)
            else:
                root.val = root.right.val
                root.right = root.right.right
        
        return root