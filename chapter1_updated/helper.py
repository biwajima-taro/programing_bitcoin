import hashlib
from script import Script
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


def encode_variant(length_: int):
    if length_ < 0xfd:
        return bytes([length_])
    elif length_ < 0x10000:
        return b"\xfd"+int_to_little_endian(length_, 2)
    elif length_ < 0x100000000:
        return b"\xfe"+int_to_little_endian(length_, 4)
    elif length_ < 0x10000000000000000:
        return b"\xff"+int_to_little_endian(length_, 8)
    else:
        raise ValueError(f"integer too large {length_}")


def decode_base58(s):
    num = 0
    for c in s:
        num *= 58
        # index returns index  of c
        num += BASE58_ALPHABET.index(c)
    combined = num.to_bytes(25, byteorder="big")
    checksum = combined[-4:]
    actual = hash256(combined[:-4])[:4]
    if actual != checksum:
        raise ValueError("bad address!  {actual}!={checksum}")
    return combined


def p2pkh_script(h160: bytes):
    return Script([0x76, 0xa9, h160, 0x88, 0xac])
