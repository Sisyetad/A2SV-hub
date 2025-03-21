# Problem: Find Largest Value in Each Tree Row - https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        self.values = defaultdict(lambda: float('-inf'))
        def helper(root,i):
            if not root:
                return 
                
            self.values[i] = max(self.values[i],root.val)
            helper(root.left,i+1)
            helper(root.right,i+1)
        helper(root,0)
        return [self.values[key] for key in self.values]