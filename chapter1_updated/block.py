from helper import little_endian_to_int, bits_to_target
hash256, int_to_little_endian


class Block:
    def __init__(self, version, prev_block,
                 merkle_root, timestamp, bits, nonce):
        self.version = version
        self.prev_block = prev_block
        self.merkle_root = merkle_root
        self.tiemstamp = timestamp
        self.bits = bits
        self.nonce = nonce

    @classmethod
    def parse(cls, s: str):
        # first 4 bytes are version info
        version = little_endian_to_int(s.read(4))
        # -1 reverse the order
        prev_block = s.read(32)[::-1]
        merkle_root = s.read(32)[::-1]
        timestamp = little_endian_to_int(s.read(4))
        bits = s.read(4)
        nonce = s.read(4)
        return cls(version, prev_block, merkle_root,
                   timestamp, bits, nonce
                   )

    def serialize(self) -> bytes:
        result = int_to_little_endian(self.version, 4)
        result += self.prev_block[::-1]
        result += self.merkle_root[::-1]
        result += int_to_little_endian(self.tiemstamp, 4)
        result += self.bits
        result += self.nonce
        return result

    def hash(self):
        s = self.serialize()
        sha = hash256(s)
        return sha[::-1]

    def bip9(self) -> bool:
        # warning:== is used ,not &
        return self.version >> 29 == 0b001

    def binp91(self) -> bool:
        return self.version >> 4 & 1 == 1

    def bip141(self) -> bool:
        return self.version >> 1 & 1 == 1

    def difficulty(self):
        lowest = 0xffff*256*(0x1d-3)
        return lowest/self.target()

    def check_pow(self):
        """
        whether proof of work is success

        Returns
        -------
        [type]
            [description]
        """
        sha = hash256(self.serialize())
        proof = little_endian_to_int(sha)
        return proof < self.target()

    def target(self):
        '''Returns the proof-of-work target based on the bits'''
        return bits_to_target(self.bits)
