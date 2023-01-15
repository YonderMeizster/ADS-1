class NativeCache:
    def __init__(self, sz = 103):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size
        self.step = 5

    def __str__(self):
        pairs = [f'{self.slots[i]} : {self.values[i]}, {self.hits[i]}' for i in
                 range(self.size) if self.slots[i] is not None]
        answer = ' '.join(pairs)

        return '{' + f'{answer}' + '}'

    def _remove(self, index):
        self.slots[index] = self.values[index] = None
        self._clean_hits(index)

    def _clean_hits(self, index):
        self.hits[index] = 0
    
    def hash_fun(self, value):
        hash_sum = 0
        for char in value:
            hash_sum = ((hash_sum * 17) + ord(char)) % self.size
        return hash_sum

    def clean_slot(self, index):
        min_hits = self.hits[index]
        min_hits_index = index
        
        index = (index + self.step) % self.size
        curr = index
        while curr != index:
            if self.hits[curr] < min_hits:
                min_hits = self.hits[curr]
                min_hits_index = curr
            curr = (curr + self.step) % self.size
        self._remove(min_hits_index)
        return min_hits_index

    def get_the_slot(self, key, value):
        index = self.hash_fun(key)
        if self.slots[index] is None:
            return index
        if self.slots[index] == key:
                return
        start = index
        index = (index + self.step) % self.size
        while index != start:
            if self.slots[index] is None:
                return index
            if self.slots[index] == key:
                return
            index = (index + self.step) % self.size
        return self.clean_slot(index)

    def put(self, key, value):
        prev_index = self.find(key)
        if isinstance(prev_index, int):
            self.

        index = self.get_the_slot(key, value)
        if index is None:
            return
        self.slots[index] = key
        self.values[index] = value

    def get(self, key):
        index = self.find(key)
        if index is None:
            return None
        self.hits[index] += 1
        return self.values[index]

    def find(self, key):
        index = self.hash_fun(key)
        if self.slots[index] == key:
            return index
        start = index
        index = (index + self.step) % self.size
        while index != start:
            if self.slots[index] == key:
                return index
            index = (index + self.step) % self.size
        return