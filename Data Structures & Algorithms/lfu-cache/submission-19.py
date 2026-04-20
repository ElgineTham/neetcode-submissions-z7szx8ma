class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev, self.next = None, None

class LinkedList:
    def __init__(self):
        self.cache = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
    
    def length(self):
        return len(self.cache)
    
    def insert(self, node):
        self.cache[node.key] = node
        prev = self.right.prev
        prev.next, self.right.prev = node, node
        node.prev, node.next = prev, self.right
    
    def popleft(self):
        node = self.left.next
        popped = self.cache.pop(node.key)
        self.left.next = node.next
        node.next.prev = self.left
        return popped
    
    def remove(self, node):
        self.cache.pop(node.key)
        prev, aft = node.prev, node.next
        prev.next, aft.prev = aft, prev

class LFUCache:

    def __init__(self, capacity: int):
        self.key_to_node = {}
        self.freq_to_list = defaultdict(LinkedList)
        self.cap = capacity
        self.lowest_freq = 0

    def counter(self, node):
        cnt = node.freq
        self.freq_to_list[cnt].remove(node)

        if cnt == self.lowest_freq and self.freq_to_list[cnt].length() == 0:
            self.lowest_freq += 1
        
        node.freq += 1
        self.freq_to_list[node.freq].insert(node)
        

    def get(self, key: int) -> int:
        if key in self.key_to_node:
            self.counter(self.key_to_node[key])
            return self.key_to_node[key].val
        
        return -1

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        
        if key in self.key_to_node:
            self.key_to_node[key].val = value
            self.counter(self.key_to_node[key])
            return
        
        if len(self.key_to_node) == self.cap:
            popped = self.freq_to_list[self.lowest_freq].popleft()
            self.key_to_node.pop(popped.key)

        node = Node(key, value)
        self.key_to_node[key] = node
        self.freq_to_list[1].insert(node)
        self.lowest_freq = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)