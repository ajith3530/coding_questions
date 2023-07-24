from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru_cache = OrderedDict()

    def get(self, key: int) -> int:
        if self.lru_cache.get(key) is not None:
            self.lru_cache.move_to_end(key)
            return self.lru_cache.get(key)
        return -1
    def put(self, key: int, value: int) -> None:
        # Make sure to delete the entry, and treat it as a new entry
        if key in self.lru_cache:
            self.lru_cache.pop(key)
        if len(self.lru_cache) >= self.capacity:
            self.lru_cache.popitem(False)
        self.lru_cache[key] = value


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(1, 1)
obj.put(2, 2)
obj.get(1)
obj.put(3, 3)
obj.get(2)
obj.put(4, 4)
obj.get(1)
obj.get(3)
obj.get(4)

