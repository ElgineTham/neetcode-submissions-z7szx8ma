class LRUCache:

    def __init__(self, capacity: int):
        self.max_size = capacity
        self.cache = {}
        self.time_check = deque()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.time_check.remove(key)
        self.time_check.append(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.time_check.remove(key)
            self.time_check.append(key)
        else:
            if len(self.cache) == self.max_size:
                key_to_remove = self.time_check.popleft()
                del self.cache[key_to_remove]
            
            self.cache[key] = value
            self.time_check.append(key)
        
