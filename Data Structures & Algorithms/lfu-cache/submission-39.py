class Node: 
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev, self.next = None, None
        self.freq = 1

class LinkedList:
    def __init__(self):
        self.left, self.right = Node(0,0), Node(0,0)
        self.cache = {}  # {key : node}
        self.left.next = self.right
        self.right.prev = self.left
    
    def length(self):
        return len(self.cache)
    
    def insert(self, node):
        last = self.right.prev
        last.next, node.prev = node, last
        self.right.prev, node.next = node, self.right
        self.cache[node.key] = node
    
    def remove(self, node):
        popped = self.cache.pop(node.key)
        before, after = popped.prev, popped.next
        before.next = after
        after.prev = before
    
    def popleft(self):
        if self.length() == 0:
            return
        
        popped = self.left.next
        self.cache.pop(popped.key)
        self.left.next = popped.next
        popped.next.prev = self.left

        return popped

class LFUCache:

    def __init__(self, capacity: int):
        self.key_to_node = {}
        self.freq_to_list = defaultdict(LinkedList)
        self.lowest_freq = 0
        self.cap = capacity
    
    def counter(self, node):
        self.freq_to_list[node.freq].remove(node)

        if node.freq == self.lowest_freq and self.freq_to_list[node.freq].length() == 0:
            self.lowest_freq += 1
        
        node.freq += 1
        self.freq_to_list[node.freq].insert(node)

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        
        node = self.key_to_node[key]
        self.counter(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.val = value
            self.counter(node)
            return
        
        if len(self.key_to_node) == self.cap:
            popped = self.freq_to_list[self.lowest_freq].popleft()
            self.key_to_node.pop(popped.key)
        
        node = Node(key, value)
        self.lowest_freq = 1
        self.key_to_node[key] = node
        self.freq_to_list[1].insert(node)
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)