class HashTable:
    def __init__(self, sz, stp):
        if sz <= 0:
            return None
        if stp <= 0:
            return None
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        id = 0
        for char in value:
            id += ord(char)
        return id % self.size

    def seek_slot(self, value):
        index = self.hash_fun(value)
        visited_slots = []
        while self.slots[index]:
            if index in visited_slots:
                return None
            visited_slots.append(index)
            index = (index + self.step) % self.size
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
        curr_slot = (supposed_slot + self.step) % self.size
        while curr_slot != supposed_slot:
            if self.slots[curr_slot] == value:
                return curr_slot
            curr_slot = (curr_slot + self.step) % self.size
        return None


class PowerSet(HashTable):
    # I inherit the HashTable class this way because of the
    # implementation of the check server
    def __init__(self):
        self.multiplier = 2
        # 211 because of its magical meaning. Joke. You can smile
        # after all. 29 is magic too
        super().__init__(211, 29)

    def seek_slot(self, value):
        if not self.get(value):
            return self.hash_fun(value)
        index = self.hash_fun(value)
        return (len(self.slots) // index) * index + self.step

    def put(self, value):
        # Проверить, есть ли значение в слотах
        if self.get(value):
            return
        index = self.seek_slot(value)
        if index > len(self.slots)
        self.slots[index] = value

    def get(self, value):
        index = self.hash_fun(value)
        while index < len(self.slots):
            if index == self.slots[index]:
                return True
            index += self.step
        return False
    
    def size(self):
        pass

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
