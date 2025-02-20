# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy1 = ListNode(0)
        dummy2 = ListNode(0)
        dummy1.next = list1
        dummy2.next = list2
        current = dummy
        current1 = dummy1.next
        current2 = dummy2.next
        while current1 and current2:
            if current1.val < current2.val:
                current.next = current1
                current1 = current1.next
            else:
                current.next = current2
                current2 = current2.next
            current = current.next
        while current1:
            current.next = current1
            current1 = current1.next
            current = current.next
        while current2:
            current.next = current2
            current2 = current2.next
            current = current.next
        return dummy.next