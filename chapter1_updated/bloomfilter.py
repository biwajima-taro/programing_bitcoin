0BIP37_CONSTANT = 0xfba4c795


class BloomFilter:
    def __init__(self, size, function_count, tweak):
        self.size = size
        self.bit_field = [0]*(8*size)
        self.function_count = function_count
        self.tweak = tweak
