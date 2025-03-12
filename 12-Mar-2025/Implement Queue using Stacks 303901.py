# Problem: Implement Queue using Stacks - https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.queue = []
        self.head = 0
        self.n = 0

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.n += 1

    def pop(self) -> int:
        poped = self.queue[self.head]
        self.head += 1
        return poped

    def peek(self) -> int:
        return self.queue[self.head]

    def empty(self) -> bool:
        if self.head == self.n:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()