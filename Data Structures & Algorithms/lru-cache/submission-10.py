class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.size = capacity
        self.time_check = deque()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.time_check.remove(key)
        self.time_check.append(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if len(self.cache) == self.size:
                key_to_remove = self.time_check.popleft()
                self.cache.pop(key_to_remove)
            self.cache[key] = value
            self.time_check.append(key)
        else:
            self.get(key)
            self.cache[key] = value