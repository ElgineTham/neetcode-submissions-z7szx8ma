class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
        self.cap = capacity
        self.size = 0
        self.hash_map = {}

    def get(self, key: int) -> int:
        if key in self.hash_map:
            node = self.hash_map[key]
            prev, aft = node.prev, node.next
            prev.next = aft
            aft.prev = prev
            
            temp = self.left.next
            self.left.next = node
            node.prev = self.left
            node.next = temp
            temp.prev = node
            return node.val
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            node = self.hash_map[key]
            prev, aft = node.prev, node.next
            prev.next = aft
            aft.prev = prev
            
            node.val = value

            temp = self.left.next
            self.left.next = node
            node.prev = self.left
            node.next = temp
            temp.prev = node
        else:
            node = Node(key, value)
            self.hash_map[key] = node
            temp = self.left.next
            self.left.next = node
            node.prev = self.left
            node.next = temp
            temp.prev = node

            self.size += 1

            while self.size > self.cap:
                remove = self.right.prev
                remove.prev.next = self.right
                self.right.prev = remove.prev
                del self.hash_map[remove.key]
                self.size -= 1


