class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def insert(self, node):
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        self.right.prev = node
        node.next = self.right
    
    def remove(self, node):
        prev, aft = node.prev, node.next
        prev.next = aft
        aft.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.cache.pop(key)
        
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.cap:
            self.cache.pop(self.left.next.key)
            self.remove(self.left.next)
    

                
        
