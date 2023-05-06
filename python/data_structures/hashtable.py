
class Hashtable:

    def __init__(self, size=1024):
        self._size = size
        self._buckets = size * [None]

    def set(self, key, value):
        index = self.hash(key)
        if not self._buckets[index]:
            self._buckets[index] = []
        self._buckets[index].append((key, value))

    def get(self, key):
        index = self.hash(key)
        if self._buckets[index]:
            for k, v in self._buckets[index]:
                if k == key:
                    return v
        raise KeyError(f"Key '{key}' not found")

    def has(self, key):
        index = self.hash(key)
        if self._buckets[index]:
            for k, _ in self._buckets[index]:
                if k == key:
                    return True
        return False

    def keys(self):
        keys = []
        for bucket in self._buckets:
            if bucket:
                for k, _ in bucket:
                    keys.append(k)
        return keys

    def hash(self, key):
        hash_total = 0
        for char in key:
            hash_total += ord(char)
        primed_number = hash_total * len(key) * 19
        index = primed_number % self._size
        return index

