class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}        # Maps key -> value
        self.usage_order = []  # List to track recency (index 0 is LRU)
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        # Move key to the end to mark it as most recently used
        self.usage_order.remove(key)  # O(N) operation
        self.usage_order.append(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update value and move key to the end
            self.usage_order.remove(key)  # O(N) operation
        else:
            if len(self.cache) >= self.capacity:
                # Evict the least recently used (first item in the list)
                lru_key = self.usage_order.pop(0)  # O(N) operation
                del self.cache[lru_key]
                
        self.cache[key] = value
        self.usage_order.append(key)
