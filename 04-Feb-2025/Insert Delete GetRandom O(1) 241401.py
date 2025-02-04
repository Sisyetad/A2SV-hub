# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/

class RandomizedSet:
    def __init__(self):
        self.data = []  # Stores values for O(1) random access
        self.index_map = {}  # Maps value -> index in `data`

    def insert(self, val: int) -> bool:
        if val in self.index_map:
            return False
        self.index_map[val] = len(self.data)
        self.data.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index_map:
            return False

        # Swap the element to delete with the last element for O(1) deletion
        last_element = self.data[-1]
        index_to_remove = self.index_map[val]

        self.data[index_to_remove] = last_element
        self.index_map[last_element] = index_to_remove  # Update index of moved element

        # Remove last element (O(1) operation)
        self.data.pop()
        del self.index_map[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.data)  # O(1) random access
