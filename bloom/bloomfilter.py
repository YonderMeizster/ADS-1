class BloomFilter:
    def __init__(self, f_len=32):
        self.filter_len = f_len
        self.bit_array = 0  # imports cannot be used. So, dirty hack time
        self.hash_funcs = (self.hash1, self.hash2)

    def _bits(self):
        return bin(self.bit_array)[2:].zfill(self.filter_len)

    def _set_bit(self, bit_array, position):
        return bit_array | (1 << position)

    def _zero_bit(self, bit_array, position):
        return bit_array & ~(1 << position)

    def hash1(self, str1):
        hash_sum = 0
        for char in str1:
            hash_sum = ((hash_sum * 17) + ord(char)) % self.filter_len
        return hash_sum

    def hash2(self, str1):
        hash_sum = 0
        for char in str1:
            hash_sum = ((hash_sum * 223) + ord(char)) % self.filter_len
        return hash_sum

    def add(self, str1):
        indexes = (hash_func(str1) for hash_func in self.hash_funcs)
        for index in indexes:
            self.bit_array = self._set_bit(self.bit_array, index)

    def is_value(self, str1):
        comparision_bits = self.bit_array
        flag = False
        indexes = (hash_func(str1) for hash_func in self.hash_funcs)
        for index in indexes:
            comparision_bits = self._zero_bit(comparision_bits, index)
        return not comparision_bits == self.bit_array
