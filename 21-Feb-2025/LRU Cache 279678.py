# Problem: LRU Cache - https://leetcode.com/problems/lru-cache/

class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  
        self.head = Node()  
        self.tail = Node()  
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        previous_node, next_node = node.prev, node.next
        previous_node.next = next_node
        next_node.prev = previous_node

    def _add_to_end(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)  
            self._add_to_end(node)  
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_end(node)
        else:
            if len(self.cache) >= self.capacity:
                lru_node = self.head.next
                del self.cache[lru_node.key]
                self._remove(lru_node)
            
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_end(new_node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

