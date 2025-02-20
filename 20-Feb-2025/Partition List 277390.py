# Problem: Partition List - https://leetcode.com/problems/partition-list/

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before_head = before = ListNode(0) 
        after_head = after = ListNode(0)  

        current = head
        while current:
            if current.val < x:
                before.next = current
                before = before.next
            else:
                after.next = current
                after = after.next
            current = current.next

        after.next = None 
        before.next = after_head.next  

        return before_head.next 
