class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        id = 0
        for char in key:
            id += ord(char)
        return id % self.size

    def is_key(self, key):
        slot_id = self.hash_fun(key)        
        return self.slots[slot_id] == key

    def put(self, key, value):
        slot_id = self.hash_fun(key)
        self.slots[slot_id] = key
        self.values[slot_id] = value

    def get(self, key):
        if not self.is_key(key):
            return None
        slot_id = self.hash_fun(key)
        return self.values[slot_id]

