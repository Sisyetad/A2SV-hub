# Problem: Design Circular Deque - https://leetcode.com/problems/design-circular-deque/

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class MyCircularDeque:

    def __init__(self, k: int):
        self.size = k
        self.count = 0
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
    def insertFront(self, value: int) -> bool:
        if self.count < self.size:
            self.count += 1
            new_node = Node(value)
            new_node.next = self.head.next
            self.head.next.prev = new_node
            self.head.next = new_node
            new_node.prev = self.head
            return True
        else:
            return False


    def insertLast(self, value: int) -> bool:
        if self.count < self.size:
            self.count += 1
            new_node = Node(value)
            new_node.prev = self.tail.prev
            self.tail.prev.next = new_node
            self.tail.prev = new_node
            new_node.next = self.tail
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if self.count > 0:
            self.count -= 1
            self.head.next = self.head.next.next
            self.head.next.prev = self.head
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        if self.count > 0:
            self.count -= 1
            self.tail.prev = self.tail.prev.prev
            self.tail.prev.next = self.tail
            return True
        else:
            return False

    def getFront(self) -> int:
        if self.count > 0:
            return self.head.next.val
        return -1

    def getRear(self) -> int:
        if self.count > 0:
            return self.tail.prev.val
        return -1

    def isEmpty(self) -> bool:
        return self.count == 0
        

    def isFull(self) -> bool:
        return self.count == self.size


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()