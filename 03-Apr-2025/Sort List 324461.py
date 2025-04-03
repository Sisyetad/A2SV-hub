# Problem: Sort List - https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        def merge(left_half, right_half):
            merged = curr = ListNode()
            while left_half and right_half:
                if left_half.val <= right_half.val:
                    new_node = ListNode(left_half.val)
                    curr.next = new_node
                    curr = curr.next
                    left_half = left_half.next
                else:
                    new_node = ListNode(right_half.val)
                    curr.next = new_node
                    curr = curr.next
                    right_half = right_half.next
            if left_half:
                curr.next = left_half
            if right_half:
                curr.next = right_half
            return merged.next

        def merge_sort(root):
            if root and not root.next:
                return root
            
            slow = fast = ListNode(0)
            slow.next = root
            fast.next = root
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            temp = slow.next
            slow.next = None
            
            left_half = merge_sort(root)
            right_half = merge_sort(temp)
            return merge(left_half, right_half)
        return merge_sort(head)
