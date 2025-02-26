# Problem: Design Browser History - https://leetcode.com/problems/design-browser-history/description/

class Node:
    def __init__(self,url):
        self.val = url
        self.next = None
        self.prev = None
class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = Node(homepage)
        self.position = 0

    def visit(self, url: str) -> None:
        new_node = Node(url)
        count = 0
        current = self.homepage
        while current and count < self.position:
            count += 1
            current = current.next
        current.prev = new_node
        new_node.next = current
        self.homepage = new_node 
        self.position = 0
        

    def back(self, steps: int) -> str:
        current = self.homepage
        steps += self.position
        self.position = 0
        while current and current.next and self.position < steps:
            current = current.next
            self.position  += 1
        return current.val

    def forward(self, steps: int) -> str:
        current = self.homepage
        steps = self.position - steps
        self.position = 0
        count = 0
        while current and current.next and self.position < steps:
            current = current.next
            self.position  += 1
        return current.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)