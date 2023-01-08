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
