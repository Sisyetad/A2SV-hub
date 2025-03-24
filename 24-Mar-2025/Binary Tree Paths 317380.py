# Problem: Binary Tree Paths - https://leetcode.com/problems/binary-tree-paths/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.res = []
        def helper(root, path):
            if not root:
                return
            
            path.append(str(root.val))
            if not root.left and not root.right:
                self.res.append('->'.join(path))
            
            helper(root.left,path) 
            helper(root.right,path)
            path.pop()
            
        helper(root,[])
        return self.res