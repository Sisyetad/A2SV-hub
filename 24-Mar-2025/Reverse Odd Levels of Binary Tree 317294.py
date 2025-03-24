# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

class Solution:
    def reverseOddLevels(self, root):
        if not root:
            return None 

        queue = deque([root])
        level = 0

        while queue:
            size = len(queue)
            current_level_nodes = []

            for _ in range(size):
                node = queue.popleft()
                current_level_nodes.append(node)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level % 2:
                left, right = 0, len(current_level_nodes) - 1
                while left < right:
                    tmp = current_level_nodes[left].val
                    current_level_nodes[left].val = current_level_nodes[
                        right
                    ].val
                    current_level_nodes[right].val = tmp
                    left += 1
                    right -= 1

            level += 1

        return root