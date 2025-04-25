# Problem: Binary Tree Level Order Traversal - https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        queue = deque([(root, 0)])
        ans = []
        while queue:
            node = queue.popleft()

            if node[0]:
                if node[1] == len(ans):
                    ans.append([])
                ans[node[1]].append(node[0].val)
                queue.append((node[0].left, node[1] + 1))
                queue.append((node[0].right, node[1] + 1))
                
        return ans