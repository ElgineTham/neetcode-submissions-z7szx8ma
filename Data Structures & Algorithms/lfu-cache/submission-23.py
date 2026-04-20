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
        self.left.next = self.right
        self.right.prev = self.left
    
    def length(self):
        return len(self.cache)
    
    def insert(self, node):
        self.cache[node.key] = node
        prev = self.right.prev
        prev.next = node
        self.right.prev = node
        node.prev = prev
        node.next = self.right
    
    def remove(self, node):
        self.cache.pop(node.key)
        prev, aft = node.prev, node.next
        prev.next = aft
        aft.prev = prev
    
    def popleft(self):
        node_to_remove = self.left.next
        self.cache.pop(node_to_remove.key)
        self.left.next = node_to_remove.next
        node_to_remove.next.prev = self.left
        return node_to_remove


class LFUCache:

    def __init__(self, capacity: int):
        self.lowest_freq = 0
        self.key_to_node = {}
        self.freq_to_list = defaultdict(LinkedList)
        self.cap = capacity
    
    def counter(self, node):
        cnt = node.freq
        self.freq_to_list[cnt].remove(node)

        if self.lowest_freq == cnt and self.freq_to_list[cnt].length() == 0:
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
            node = self.key_to_node[key]
            self.counter(node)
            node.val = value
            self.key_to_node[key] = node
            return
        
        if len(self.key_to_node) == self.cap:
            popped = self.freq_to_list[self.lowest_freq].popleft()
            self.key_to_node.pop(popped.key)
        
        self.lowest_freq = 1
        node = Node(key, value)
        self.key_to_node[key] = node
        self.freq_to_list[1].insert(node)



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)