import hashlib

BASE58_ALPHABET = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'


def encode_base58(s: bytes) -> str:
    # count how many 0 are at start
    count = 0
    for c in s:
        if c == 0:
            count += 1
        else:
            break
        prefix = "1"*count
        num = int.from_bytes(s, "big")
        result = ""
        while num > 0:
            num, mod = divmod(num, 58)
            result = BASE58_ALPHABET[mod]+result
        return prefix+result


def hash256(s):
    '''two rounds of sha256'''
    return hashlib.sha256(hashlib.sha256(s).digest()).digest()


def encode_base58_checksum(adress: bytes):
    return encode_base58(adress+hash256(adress)[:4])


def hash160(s):
    '''sha256 followed by ripemd160'''
    return hashlib.new('ripemd160', hashlib.sha256(s).digest()).digest()


def little_endian_to_int(b: bytes):
    return int.from_bytes(b, "little")


def int_to_little_endian(n: int, length: int):
    return n.to_bytes(length, "little")


def read_variant(s):
    i = s.read(1)[0]
    if i == 0xfd:
        return little_endian_to_int(s.read(2))
    