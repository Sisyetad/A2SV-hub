# Problem: Odd Even Linked List - https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = first = ListNode(0)
        even = second = ListNode(0)
        count = 1
        current = head
        while current:
            if count%2:
                first.next = current
                first = first.next
            else:
                second.next = current
                second = second.next
            current = current.next
            count += 1
        second.next = None
        first.next = even.next
        return odd.next