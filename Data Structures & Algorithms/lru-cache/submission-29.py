class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev, self.next = None, None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
    

    def insert(self, node):
        last = self.right.prev
        last.next = node
        self.right.prev = node
        node.prev = last
        node.next = self.right

        self.cache[node.key] = node
    

    def remove(self, node):
        if node.key not in self.cache:
            return
            
        self.cache.pop(node.key)

        bfr, aft = node.prev, node.next
        bfr.next = aft
        aft.prev = bfr
    

    def popleft(self):
        if len(self.cache) == 0:
            return
        
        popped = self.left.next
        self.left.next = popped.next
        popped.next.prev = self.left

        self.cache.pop(popped.key)
        return popped


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.remove(node)
        self.insert(node)

        return node.val


    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        
        if key in self.cache:
            node = self.cache[key]
            node.val = value

            self.remove(node)
            self.insert(node)

            return
        
        if len(self.cache) == self.cap:
            popped = self.popleft()
            self.remove(popped)
        
        node = Node(key, value)
        self.insert(node)    

        
