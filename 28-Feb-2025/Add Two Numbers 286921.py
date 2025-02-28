# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = res = ListNode(0)
        curr1 = l1
        curr2 = l2
        quetient = 0
        while curr1 or curr2:
            temp = (curr1.val if curr1 else 0) + (curr2.val if curr2 else 0) + quetient
            rem = temp % 10
            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None
            new_node = ListNode(rem)
            quetient = temp // 10
            res.next = new_node
            res = res.next
        if quetient:
            new_node = ListNode(quetient)
            res.next = new_node
        return ans.next