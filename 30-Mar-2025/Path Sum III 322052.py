# Problem: Path Sum III - https://leetcode.com/problems/path-sum-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        self.count = 0
        def helper(root, curr_sum, prefix_sum):
            if not root:
                return 

            curr_sum += root.val
            if (curr_sum - targetSum) in prefix_sum:
                self.count += prefix_sum[curr_sum - targetSum]
            prefix_sum[curr_sum] += 1
            helper(root.left, curr_sum, prefix_sum)
            helper(root.right, curr_sum, prefix_sum)
            prefix_sum[curr_sum] -= 1
            if prefix_sum[curr_sum] == 0:
                del prefix_sum[curr_sum]
            
        helper(root, 0, prefix_sum)
        return self.count