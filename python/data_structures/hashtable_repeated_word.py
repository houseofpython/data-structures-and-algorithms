




class first_repeated_word:

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

    def add_key(self, key):
        index = self.hash(key)
        if self._buckets[index] is None:
            self._buckets[index] = (key, 1)
        else:
            return key


    def get_repeated(self):
        new_list = []
        for bucket in self._buckets:
            if bucket is not None:
                print(len(bucket), 'bucket-length')
                for key, frequency in bucket:
                    if frequency > 1:
                        new_list.append(key)
                        break
        return new_list


sentence = 'Once upon a time, there was a brave princess who...'

if __name__ == '__main__':
    hashing = first_repeated_word(5000)
    for word in sentence.lower().split():
        word = word.strip('\"').replace(',','')
        check = hashing.add_key(word)
        if isinstance(check, str):
            print(f'First repeated word is: {word}')
            break













