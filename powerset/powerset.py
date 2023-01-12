class PowerSet():
    def __init__(self):
        self.elements = {}

    def _get_all(self):
        all = []
        all.extend(self.elements.keys())
        return all

    def put(self, value):
        self.elements[value] = value

    def get(self, value):
        return value in self.elements.keys()

    def size(self):
        return len(self.elements.keys())

    def remove(self, value):
        if self.get(value):
            self.elements.pop(value)
            return True
        return False

    def intersection(self, set2):
        intersec = PowerSet()
        keys_set2 = set2.elements.keys()
        for key in self.elements.keys():
            if key in keys_set2:
                intersec.put(key)
        return intersec

    def union(self, set2):
        uni = PowerSet()
        keys_set2 = set2.elements.keys()
        for key in self.elements.keys():
            uni.put(key)
        for key in keys_set2:
            uni.put(key)
        return uni

    def difference(self, set2):
        # разница текущего множества и set2
        diff = PowerSet()
        keys_set2 = set2.elements.keys()
        for key in self.elements.keys():
            if key not in keys_set2:
                diff.put(key)
        return diff

    def issubset(self, set2):
        _self_keys = self.elements.keys()
        for key in set2.elements.keys():
            if key not in _self_keys:
                return False
        return True
