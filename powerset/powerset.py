class HashTable:
    def __init__(self, sz, stp):
        if sz <= 0:
            return None
        if stp <= 0:
            return None
        self.length = sz
        self.step = stp
        self.slots = [None] * self.length

    def hash_fun(self, value):
        id = 0
        for char in value:
            id += ord(char)
        return id % self.length

    def seek_slot(self, value):
        index = self.hash_fun(value)
        visited_slots = []
        while self.slots[index]:
            if index in visited_slots:
                return None
            visited_slots.append(index)
            index = (index + self.step) % self.length
        return index

    def put(self, value):
        founded_slot = self.seek_slot(value)
        if founded_slot is None:
            return None
        self.slots[founded_slot] = value
        return founded_slot

    def find(self, value):
        supposed_slot = self.hash_fun(value)
        if self.slots[supposed_slot] == value:
            return supposed_slot
        curr_slot = (supposed_slot + self.step) % self.length
        while curr_slot != supposed_slot:
            if self.slots[curr_slot] == value:
                return curr_slot
            curr_slot = (curr_slot + self.step) % self.length
        return None


class PowerSet(HashTable):
    # I inherit the HashTable class this way because of the
    # implementation of the check server
    def __init__(self):
        self.multiplier = 2
        # 211 because of its magical meaning. Joke. You can smile
        # after all. 29 is magic too
        super().__init__(2011, 5)

    def _get_all(self):
        return [value for value in self.slots if value]

    def seek_slot(self, value):
        """Looks for an index that can be used to store a value in self.slots.
        Returns suitable index out range of self.slots."""
        index = self.hash_fun(value)
        while index < len(self.slots):
            if not self.slots[index]:
                return index
            last = index
            index += self.step
        return index

    def put(self, value):
        """Puts value into set if it still not there, otherwise
        do nothing."""
        if self.get(value):
            return
        founded = self.seek_slot(value)
        if  founded >= len(self.slots):
            self.slots.extend([None] * int(len(self.slots) * 0.3))
        self.slots[founded] = value

    def get(self, value):
        """Returns True if the value is stored in self.slots,
        otherwise False."""
        return value in self.slots

    def size(self):
        return len([x for x in self.slots if x])
        

    def remove(self, value):
        # возвращает True если value удалено
        # иначе False
        return False

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
