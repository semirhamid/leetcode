class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.current_size = 0
        self.left = Node(0, 0) 
        self.right = Node(0, 0) 
        self.left.next = self.right
        self.right.prev = self.left
        self.cache = {}

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        elif len(self.cache) == self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        new_node = Node(key, value)
        self.insert(new_node)
        self.cache[key] = new_node
