# Problem: Sum of Nodes with Even-Valued Grandparent - https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        ans = 0
        while queue:
            n = len(queue)
            grand_child = []
            for _ in range(n):
                poped = queue.popleft()
                if poped.val%2 == 0:
                    if poped.left:
                        grand_child.append(poped.left.left)
                        grand_child.append(poped.left.right)
                    if poped.right:
                        grand_child.append(poped.right.left)
                        grand_child.append(poped.right.right)
                if poped.left:
                    queue.append(poped.left)
                if poped.right:
                    queue.append(poped.right)
            if grand_child:
                for child in grand_child:
                    if child:
                        ans += child.val

        return ans