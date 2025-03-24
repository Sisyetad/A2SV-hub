# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        level = 0
        curr = []
        result = []
        while queue:
            n = len(queue)
            curr = []
            
            for _ in range(n):
                poped = queue.popleft()
                curr.append(poped)

                if poped.left:
                    queue.append(poped.left)
                if poped.right:
                    queue.append(poped.right)
            
            if level%2:
                r = len(curr) - 1
                while r >= 0:
                    if level == len(result):
                        result.append([])
                    result[level].append(curr[r].val)
                    r -= 1
            else:
                l = 0
                while l < len(curr):
                    if level == len(result):
                        result.append([])
                    result[level].append(curr[l].val)
                    l += 1
            level += 1
        return result