class PowerSet():
    def __init__(self):
        self._size = 100009
        self.slots = [[None] for _ in range(self._size)]

    def hash_fun(self, value):
        id = 0
        for char in value:
            id += ord(char)
        return id % self._size

    def _get_all(self):
        values = []
        size = 0
        for slot in self.slots:
            for value in slot:
                if value is not None:
                    values.append(value)
                    size += 1
        return {'values' : values, 'size' : size}

    def put(self, value):
        if self.get(value):
            return
        
        slot = self.hash_fun(value)
        
        if self.slots[slot][0] is None:
            self.slots[slot][0] = value
            return
        self.slots[slot].append(value)

    def get(self, value):
        slot = self.hash_fun(value)
        return value in self.slots[slot]

    def size(self):
        return self._get_all()['size']

    def remove(self, value):
        if not self.get(value):
            return False
        
        slot = self.hash_fun(value)

        self.slots[slot].remove(value)
        return True

    def intersection(self, set2):
        # пересечение текущего множества и set2
        return None

    def union(self, set2):
        # объединение текущего множества и set2
        return None

    def difference(self, set2):
        # разница текущего множества и set2
        return None

    def issubset(self, set2):
        # возвращает True, если set2 есть
        # подмножество текущего множества,
        # иначе False
        return False
