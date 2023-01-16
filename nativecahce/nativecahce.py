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

    def _check_slots(self, index, condition):
        if condition(index):
            return index

        start = index
        index = (index + self.step) % self.size

        while index != start:
            if condition(index):
                return index
            index = (index + self.step) % self.size

    def hash_fun(self, value):
        hash_sum = 0
        for char in str(value):
            hash_sum = ((hash_sum * 17) + ord(char)) % self.size
        return hash_sum

    def keys(self):
        _keys = []
        for key in self.slots:
            if key is not None:
                _keys.append(key)
        return _keys

    def clean_slot(self, index):
        min_hits = self.hits[index]
        min_hits_index = index

        start = index
        index = (index + self.step) % self.size

        while index != start:
            if self.hits[index] < min_hits:
                min_hits = self.hits[index]
                min_hits_index = index
            index = (index + self.step) % self.size
        self._remove(min_hits_index)
        return min_hits_index

    def get_slot(self, key, value):
        index = self.hash_fun(str(key))
        def condition(index): return self.slots[index] is None

        produced_index = self._check_slots(index, condition)
        if isinstance(produced_index, int):
            return produced_index

        return self.clean_slot(index)

    def put(self, key, value):
        key = str(key)
        prev_index = self.find(key)

        if isinstance(prev_index, int):
            self.slots[prev_index] = key
            self.values[prev_index] = value
            self._clean_hits(prev_index)
            return

        index = self.get_slot(key, value)
        self.slots[index] = key
        self.values[index] = value

    def get(self, key):
        key = str(key)
        index = self.find(key)
        if index is None:
            return None
        self.hits[index] += 1
        return self.values[index]

    def find(self, key):
        key = str(key)
        index = self.hash_fun(key)
        def condition(index): return self.slots[index] == key
        return self._check_slots(index, condition)
