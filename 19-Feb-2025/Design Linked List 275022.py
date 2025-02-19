# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.dummy = Node("dummy")
        self.size = 0

    def get(self, index: int) -> int:
        count = -1
        current = self.dummy
        while current and count < index:
            current = current.next
            count += 1
        return current.value if current else -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.dummy.next
        self.dummy.next = new_node

    def addAtTail(self, val: int) -> None:
        current = self.dummy
        new_node = Node(val)
        while current.next:
            current = current.next
        current.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        current = self.dummy
        count = 0
        new_node = Node(val)
        while current and count < index:
            current = current.next
            count += 1
        if current:
            new_node.next = current.next
            current.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        current = self.dummy
        count = 0
        while current and current.next and count < index:
            current = current.next
            count += 1
        if current and current.next:
            current.next = current.next.next
        else:
            current.next = None


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)