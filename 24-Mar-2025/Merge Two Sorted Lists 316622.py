# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, L1: Optional[ListNode], L2: Optional[ListNode]) -> Optional[ListNode]:
        
        self.curr = dummy = ListNode(0)
        def helper(L1, L2):
            if not L1 and not L2:
                return
            if not L1:
                self.curr.next = ListNode(L2.val)
                self.curr = self.curr.next
                helper(L1, L2.next)
            elif not L2:
                self.curr.next = ListNode(L1.val)
                self.curr = self.curr.next
                helper(L1.next, L2)
            elif L1.val < L2.val:
                self.curr.next = ListNode(L1.val)
                self.curr = self.curr.next
                helper(L1.next, L2)
                
            else:
                self.curr.next = ListNode(L2.val)
                self.curr = self.curr.next
                helper(L1, L2.next)
        helper(L1,L2)
        return dummy.next